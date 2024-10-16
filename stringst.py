import streamlit as st

st.title("String Example")

# String input
string_value = st.text_input("Enter a string:", value="Hello, Streamlit!")
st.text_input("hello")
# Display the string value
st.write(f"The string you entered is: {string_value}")
