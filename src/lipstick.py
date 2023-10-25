import time
import streamlit as st
from langchain.utilities.dalle_image_generator import DallEAPIWrapper
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from PIL import Image
#from streamlit_feedback import streamlit_feedback
import requests
from io import BytesIO
from colors import hex2rgb, NAMES_ORIGINAL
from prompts import ZERO_SHOT_PROMPT_TEMPLATE, FEW_SHOT_PROMPT_TEMPLATE, MANY_SHOT_PROMPT_TEMPLATE, IMAGE_AD_PROMPT

st.session_state['openai_api_key'] = ''
if 'OPENAI_API_KEY' in st.secrets:
    st.session_state['openai_api_key'] = st.secrets['OPENAI_API_KEY']

PROMPTS = {'zero-shot': ZERO_SHOT_PROMPT_TEMPLATE, 'few-shot': FEW_SHOT_PROMPT_TEMPLATE, 'many-shot': MANY_SHOT_PROMPT_TEMPLATE}

# def _save_feedback(feedback):
#     with st.spinner('Saving feedback...'):
#         time.sleep(2)
#     st.success('Done!')
#     print(feedback)

def generate_ad_image(color_rgb: str, name: str):
    with st.status("Calling OpenAI API...", expanded=True) as status:
        llm = OpenAI(model_name="text-davinci-003",
                    temperature=st.session_state['temperature'],
                    max_tokens=50,
                    openai_api_key=st.session_state['openai_api_key'])

        description_template = PromptTemplate.from_template(IMAGE_AD_PROMPT)
        description_prompt = description_template.format(color=color_rgb, name=name)

        status.update(label=f"Generating image description...", expanded=True)
        image_description = llm(description_prompt)

        prompt = PromptTemplate(
            input_variables=["image_desc"],
            template="{image_desc}",
        )

        status.update(label=f"Generating image...", expanded=True)
        chain = LLMChain(llm=llm, prompt=prompt)
        image_url = DallEAPIWrapper().run(chain.run(image_description))
        response = requests.get(image_url)

        status.update(label=f"Ad image generated!", state="complete", expanded=True)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption=f'Based on the generated prompt: {image_description}')

def generate_name(similar_colors_rgb: dict):
    color = st.session_state['color']
    temperature = st.session_state['temperature']
    openai_api_key = st.session_state['openai_api_key']

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

        with st.status("Calling OpenAI API...", expanded=True) as status:
            generated_name = llm(prompt)
            status.update(label=f"💄 Lipstick name generated with {prompt_name}!", state="complete", expanded=True)
            st.header(generated_name.replace('<name>',''), divider='rainbow')
            #streamlit_feedback(feedback_type="faces", key=f'{color[1:]}-{generated_name}', on_submit=_save_feedback)
            st.button(
                label="Generate Ad",
                type="primary",
                key=f"generate_ad_{prompt_name}_{color}",
                on_click=generate_ad_image,
                args=[generated_name.replace('<name>',''), hex2rgb(color)],
            )
