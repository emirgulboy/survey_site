import json
import streamlit as st
from image_loader import image_loader
st.title('A/B Testing')

if "email" not in st.session_state:
    st.session_state.email = ""
if "age" not in st.session_state:
    st.session_state.age = -1

if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

if "dataset" not in st.session_state:
    st.session_state.dataset = False

if "settings" not in st.session_state:
    with open('settings.json') as f:
        st.session_state.settings = json.load(f)

submit_button = False

if not st.session_state.form_submitted:
    with st.form(key='meta_form'):
        st.write('Please enter your name and age')
        st.write('If you want to stay anonymous, just click submit')
        email = st.text_input('Email', value=st.session_state.email)
        age = st.number_input('Age', value=st.session_state.age)
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.session_state.form_submitted = True
else:
    st.write("Thank you for submitting your information!")

if submit_button:
    st.session_state.email = email
    st.session_state.age = age
    st.session_state.form_submitted = True
    print(st.session_state.email, st.session_state.age, st.session_state.form_submitted)
    st.rerun()

if st.session_state.form_submitted and not st.session_state.dataset:

    selected_data = st.selectbox('Select Dataset', st.session_state.settings.keys())
    dataset_selected = st.button('Select Dataset')
    if dataset_selected:
        st.session_state.dataset = selected_data
        st.rerun()
    elif dataset_selected and selected_data in st.session_state.settings.keys():
        st.error('Please select a dataset')

if st.session_state.dataset:
    loader = image_loader(st.session_state.settings[st.session_state.dataset]['data_path'], st.session_state.dataset)
    st.write(loader.paths)
