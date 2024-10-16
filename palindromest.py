import streamlit as st

name=st.text_input("Enter the string to check for palindrome")

print(name)
print(name[::-1])
if name==name[::-1]:
    st.write("String is palindrome")
else:
    st.write("String is not a palindrome") 
