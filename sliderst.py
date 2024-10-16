import streamlit as st

x = st.slider('x')   #it's a widget
st.write(x,'squared is',x*x)