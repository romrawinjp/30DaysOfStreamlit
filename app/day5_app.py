import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header("st.write")

# Example 1
st.write("Hello, *World!* :sunglasses:")

# Example 2
st.write(1234)

# Example 3
df = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4], 
        "second column": [10, 20, 30, 40]
    }
)
st.write(df)

# Example 4
st.write("Below is a Data", df, "Above is a dataframe")

# Example 5
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns = ["a", "b", "c"]
)

c = alt.Chart(df2).mark_circle().encode(
    x = "a", y = "b", size = "c", color = "c", tooltip = ["a", "b", "c"]
)
st.write(c)

#--------------------------------------
st.header("st.markdown")
st.subheader("learn how to use `st.markdown`")

st.markdown("Streamlit is **_really_cool**")

#--------------------------------------
st.header("st.caption")
st.caption("This is a string that explains something above")

#---------------------------------------
st.header("st.text")
st.text('This is some text.')

#---------------------------------------
st.header("st.latex")
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

#--------------------------------------
st.header("st.code")
code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')


