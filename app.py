import streamlit as st
import numpy as np
import pandas as pd

st.title("My First Streamlit App")
value = st.slider("Select a value", 0, 100, 50)
st.write(f"You selected: {value}")

data = pd.DataFrame(np.random.randn(100, 2), columns=["x", "y"])
st.line_chart(data)

if st.button("Say Hello"):
    st.write("Hello, Streamlit!")
