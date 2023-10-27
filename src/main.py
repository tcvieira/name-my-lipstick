import openai
import streamlit as st
from streamlit_extras.badges import badge
from streamlit_extras.colored_header import colored_header
from streamlit_extras.tags import tagger_component
from colors import topk_similar_colors, rgb2hex, hex2rgb, NAMES_ORIGINAL
from lipstick import generate_name, generate_ad_image

if 'OPENAI_API_KEY' in st.secrets:
    st.session_state['openai_api_key'] = st.secrets['OPENAI_API_KEY']

st.session_state['generated_names'] = []
st.session_state['llm-image-prompt'] = False

def main():

    st.set_page_config(
	layout='centered',  # Can be 'centered' or 'wide'. In the future also 'dashboard', etc.
	initial_sidebar_state='auto',  # Can be 'auto', 'expanded', 'collapsed'
	page_title='Name My Lipstick',  # String or None. Strings get appended with '• Streamlit'.
	page_icon='💄',  # String, anything supported by st.image, or None.
    )

    # LAYOUT
    hide_menu_style = '''
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        '''
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    # horizontal radios
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} .st-emotion-cache-1qv4l6p{opacity: 1 !important;}</style>', unsafe_allow_html=True)

    # UI

    # SIDERBAR
    with st.sidebar:
        st.session_state['openai_api_key'] = st.text_input('OpenAI API Key', type='password', key="api_key_openai")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

        st.session_state['model'] = st.selectbox(
            'OpenAI model',
            ('text-davinci-003', 'gpt-3.5-turbo', 'gpt-4', 'gpt-3.5-turbo-instruct', 'gpt-3.5-turbo-16k'))

        st.session_state['llm-image-prompt'] = st.toggle('Generate image prompt with LLM')

        st.slider('Temperature', key='temperature', min_value=0.0, max_value=1.0, step=0.1, value=0.5)

    # MAIN CONTENT
    colored_header(
        label=':lipstick: Name My Lipstick',
        description='This app style transfer lipstick naming of a famous cosmetic brand',
        color_name='red-70',
    )
    tagger_component('', ['llm','openai', 'langchain', 'prompt engineering', 'style transfer'], color_name=['red', 'red', 'red', 'red', 'red'])

    badge(type='github', name='tcvieira/name-my-lipstick')

    st.markdown('---')

    st.color_picker(label='Choose a color for your lipstick', value='#9C00FF', key='color')

    if st.button(label='Generate', type='primary'):
        st.session_state['generated_names'] = []
        similar_colors_rgb = topk_similar_colors(hex2rgb(st.session_state['color']), k=5)
        'Top 5 Most Similar Colors using [CIElab](https://en.wikipedia.org/wiki/CIELAB_color_space) color space:'
        cols = st.columns(5)
        ncol = 0
        for idx, rgb_color in similar_colors_rgb.items():
            color = rgb2hex(rgb_color)
            with cols[ncol]:
                st.color_picker(label=f'similar {ncol + 1}', value=color, label_visibility="collapsed", disabled=True)
                f'{NAMES_ORIGINAL[idx]}\n{color}'
            ncol += 1
        if not st.session_state['openai_api_key']:
            st.error('No OpenAI API key provided', icon="🚨")
        else:
            try:
                generate_name(similar_colors_rgb)
                for item in st.session_state['generated_names']:
                    st.header(item['name'].replace('<name>',''), divider='rainbow')
                    st.caption(f"{item['prompt']}")
                    st.button(
                        label="Generate Ad Image",
                        type="primary",
                        key=f"generate_ad_{item['prompt']}_{item['color']}",
                        on_click=generate_ad_image,
                        args=[item['name'].replace('<name>','').upper(), hex2rgb(item['color']), st.session_state['openai_api_key'], st.session_state['temperature']],
                    )
            except openai.error.RateLimitError as e:
                retry_time = e.retry_after if hasattr(e, 'retry_after') else 60
                print()
                st.error(f'Rate limit exceeded. Retry after {retry_time} seconds...', icon="⌛️")
            except Exception as e:
                print(e)
                st.error(f'Sorry, something went wrong...', icon="😢")


if __name__ == '__main__':
    main()
