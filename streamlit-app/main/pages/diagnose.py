import requests
import streamlit as st

from config import TITLE_COLORS, SUBTITLE_COLORS, API_URL


URL = API_URL + ':8080/cvd-classification'

def fetch(session, payload):
    try:
        global URL
        result = session.post(URL, json= payload)
        return result.json()

    except Exception:
        return {}


def app():
    st.markdown(f"# <span style='color:{SUBTITLE_COLORS}'>Diagnosis</span>", unsafe_allow_html=True)

    st.write("Please, insert your data bellow and submit!!")

    session = requests.Session()

    st.markdown('### Diagnosis Form')

    with st.form("diag_form"):
    
        age = st.number_input("Age", min_value = 0, format = "%d", key="age")
        weight = st.number_input("Weight", min_value = 0.0, key="weight")
        ap_hi = st.number_input("Systolic Blood Pressure", min_value = 0, key="ap_hi")
        ap_lo = st.number_input("Diastolic blood pressure", min_value = 0, key="ap_lo")
        cholesterol = st.selectbox("Cholesterol", (1,2,3))

        
        submitted = st.form_submit_button("Submit")

        st.write("#### Diagnosis:")

        if submitted:

            payload = {
                "age": age,
                "weight": weight,
                "ap_hi": ap_hi,
                "ap_lo": ap_lo,
                "cholesterol": cholesterol,
            }

            print(payload)

            response = fetch(session, payload)

            
            if response:
                diagnosis = response['result']
                if diagnosis == 0:

                    st.markdown(f"**<span style='color:green'>Patient Without CVD!</span>**", unsafe_allow_html=True)
                
                else:
                    st.markdown(f"**<span style='color:orange'>Patient With CVD!</span>**", unsafe_allow_html=True)

