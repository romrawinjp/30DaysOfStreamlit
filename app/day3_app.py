import streamlit as st

# this will set the app header
st.header("Making simple st.button app")

if st.button("Say hello"):
    st.write("Hello there, how is your day?")
else: st.write("Good night!")