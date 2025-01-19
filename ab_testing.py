import streamlit as st

st.title('A/B Testing')

if "email" not in st.session_state:
    st.session_state.email = ""
if "age" not in st.session_state:
    st.session_state.age = -1

if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

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
    print(st.session_state.email, st.session_state.age, st.session_state.form_submitted)
    st.rerun()
