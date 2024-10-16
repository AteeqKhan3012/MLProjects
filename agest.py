import streamlit as st

res=st.slider("Choose your age",min_value=0,max_value=50,value=18,step=1)

st.write(res)