import streamlit as st
from PIL import Image
import pandas as pd
from streamlit_extras.badges import badge
from streamlit_extras.colored_header import colored_header
from streamlit_extras.tags import tagger_component
from PIL import Image
from colors import topk_similar_colors, rgb2hex, hex2rgb, color_cells, NAMES_ORIGINAL
from lipstick import generate_name

if st.secrets.has_key('OPENAI_API_KEY'): st.session_state['openai_api_key'] = st.secrets['OPENAI_API_KEY']

color_image = Image.open('img/colors.png')

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
        #st.header('Famous Brand Lipstick Name Style Generator')
        st.session_state['openai_api_key'] = st.text_input('OpenAI API Key', type='password', key="api_key_openai")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

        st.slider('Temperature', key='temperature', min_value=0.0, max_value=1.0, step=0.1, value=0.5)

    # MAIN CONTENT
    colored_header(
        label=':lipstick: Name My Lipstick',
        description='This app style transfer lipstick naming of a famous cosmetic brand',
        color_name='red-70',
    )
    tagger_component('', ['llm','openai', 'langchain', 'prompt engineering', 'style transfer'], color_name=['red', 'red', 'red', 'red', 'red'])

    #badge(type='streamlit', url='https://plost.streamlitapp.com')
    badge(type='github', name='tcvieira/name-my-lipstick')

    with st.expander('show colors from 2018 catalog'):
        st.image(color_image, caption='source: https://pinterest.com/pin/437623288787889666/')

    with st.expander('show generated cleaned dataframe'):
        df = pd.read_csv('../dataset/data_cleaned.csv')
        st.write(df.style.applymap(color_cells, subset=["color"]))

    st.markdown('---')

    st.color_picker(label='Choose a color for your lipstick', value='#ff4b4b', key='color')

    if st.button(label='Generate', type='primary'):
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
        generate_name(similar_colors_rgb)


if __name__ == '__main__':
    main()
