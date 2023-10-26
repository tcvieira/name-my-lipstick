import streamlit as st
from langchain.utilities.dalle_image_generator import DallEAPIWrapper
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from PIL import Image
import requests
from io import BytesIO
from colors import hex2rgb, NAMES_ORIGINAL
from prompts import ZERO_SHOT_PROMPT_TEMPLATE, FEW_SHOT_PROMPT_TEMPLATE, MANY_SHOT_PROMPT_TEMPLATE, IMAGE_AD_PROMPT, IMAGE_DESCRIPTION_PROMPT

st.session_state['openai_api_key'] = ''
if 'OPENAI_API_KEY' in st.secrets:
    st.session_state['openai_api_key'] = st.secrets['OPENAI_API_KEY']

PROMPTS = {'zero-shot': ZERO_SHOT_PROMPT_TEMPLATE, 'few-shot': FEW_SHOT_PROMPT_TEMPLATE, 'many-shot': MANY_SHOT_PROMPT_TEMPLATE}

def generate_ad_image(name: str, color_rgb: str):
    with st.status("Calling OpenAI API...", expanded=True) as status:
        llm = OpenAI(model_name="text-davinci-003",
                    temperature=st.session_state['temperature'],
                    max_tokens=50,
                    openai_api_key=st.session_state['openai_api_key'])

        # description_template = PromptTemplate.from_template(IMAGE_DESCRIPTION_PROMPT)
        # description_prompt = description_template.format(color=color_rgb, name=name)

        # status.update(label='Generating image description...', expanded=True)
        # image_description = llm(description_prompt)
        # print(image_description)
        # print()

        description_template = PromptTemplate.from_template(IMAGE_AD_PROMPT)
        description_prompt = description_template.format(color=color_rgb, name=name)

        prompt = PromptTemplate(
            input_variables=["image_desc"],
            template="{image_desc}",
        )

        status.update(label='Generating image...', expanded=True)
        chain = LLMChain(llm=llm, prompt=prompt)
        image_url = DallEAPIWrapper().run(chain.run(description_prompt))
        response = requests.get(image_url)
        status.update(label=f'{name}', state='complete', expanded=True)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption=f'Based on the generated prompt: {description_prompt}')
        #return img, image_description

def generate_name(similar_colors_rgb: dict):
    color = st.session_state['color']
    temperature = st.session_state['temperature']
    openai_api_key = st.session_state['openai_api_key']

    with st.status("Calling OpenAI API...", expanded=True) as status:
        for prompt_name in PROMPTS.keys():
            llm = OpenAI(model_name="text-davinci-003",
                        temperature=temperature,
                        max_tokens=50,
                        openai_api_key=openai_api_key)

            prompt_template = PromptTemplate.from_template(PROMPTS[prompt_name])
            if prompt_name == 'few-shot':
                examples = []
                for idx, rgb_color in similar_colors_rgb.items():
                    template = f"<rgb>{rgb_color}<rgb>, <name>{NAMES_ORIGINAL[idx]}<name>"
                    examples.append(template)
                prompt = prompt_template.format(color=hex2rgb(color), examples='\n'.join(examples))
            else:
                prompt = prompt_template.format(color=hex2rgb(color))

            status.update(label=f"💄 Lipstick name generated with {prompt_name}!", expanded=True)
            generated_name = llm(prompt)
            st.session_state['generated_names'].append({'name': generated_name, 'prompt': prompt_name, 'color': color})
    status.update(label=f"💄 Lipstick name generation completed!", state="complete", expanded=True)


