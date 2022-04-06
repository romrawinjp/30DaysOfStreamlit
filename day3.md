---
title: "Day 3 of Streamlit"
noteId: "0283d460b58311eca396c583453f9c51"
tags: []

---

# Day 3 of Streamlit

## `st.button`

This will set the button on the Streamlit app

## Demo app

Here is the code

    import streamlit as st

    # this will set the app header
    st.header("Making simple st.button app")

    if st.button("Say hello"):
        st.write("Hello there, how is your day?")
    else: st.write("Good night!")

## App visualization

1. Here is the display when entering the app

    ![before](./image/day3-1.png)

2. After clicking `Say hello` button

    ![after](./image/day3-2.png)
