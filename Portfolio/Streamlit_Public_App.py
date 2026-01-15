import streamlit as st

st.set_page_config(page_title="My First ML App", layout="centered")

st.title("🚀 Streamlit is Working")
st.write("Your environment, conda, and Streamlit are all set up correctly.")

name = st.text_input("What is your name?")
if name:
    st.success(f"Welcome, {name}!")

