import streamlit as st
from streamlit_option_menu import option_menu

# Custom imports 
from pages import index_page, diagnose
from config import TITLE_COLORS, SUBTITLE_COLORS

if __name__ == "__main__":

    st.set_page_config(page_title='Cardio Catch', page_icon='./images/flavi.png')

    #     # Justifying text
    st.markdown("""
    <style>
    footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)


    st.sidebar.image('./images/logo.png', use_column_width=True)

    menu_options = [
        'Welcome!', 
        'Diagnosis'
    ]
    
    menu_icons = ['house'] + ['play'] * (len(menu_options) -1)

    with st.sidebar:
        selected = option_menu("Contents", menu_options,
                           icons=menu_icons, 
                           menu_icon="list-task", 
                           default_index=0, #orientation="horizontal",
                           styles={
                                "container": {"padding": "0!important", "background-color": f"{TITLE_COLORS}"},
                                "icon": {"color": "#eee", "font-size": "14px"}, 
                                "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                "nav-link-selected": {"background-color": f"{SUBTITLE_COLORS}"},
                                "menu-title": {"color": f"#eee"}
                            })
        
    if selected == menu_options[0]:
            index_page.app()

    elif selected == menu_options[1]:
            diagnose.app()