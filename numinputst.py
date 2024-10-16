import streamlit as st

result=st.number_input("Enter any number",min_value=-10,max_value=10,step=1)

if result>0:
    st.write("This is a positive number")
elif result<0:
    st.write("This is a negative number")
else:
    st.write("This is zero")