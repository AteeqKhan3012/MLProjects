import streamlit as st
import math

num=st.number_input("Enter numer:",min_value=1,step=2)
pow=st.number_input("Enter power",min_value=0,step=1)

#math.pow(num,pow)
st.write(num**pow)