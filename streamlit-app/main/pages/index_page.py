import streamlit as st

from config import TITLE_COLORS, SUBTITLE_COLORS

def app():
    st.markdown(f"# <span style='color:{SUBTITLE_COLORS}'>Cardio Catch Disease</span>", unsafe_allow_html=True)
    st.write("We are a company specialized in detecting heart disease in the early stages.\
        We offer an early diagnosis of cardiovascular disease.")

    st.write("Would you like to try? Please, go to the Diagnosis section!")

