import streamlit as st

items=["Apples", "Oranges","Grapes","Cherry","Blueberry"]

st.title("Streamlit Application")
st.write("This is a our First Streamlit application")
st.header("This is a heading")
st.subheader("This is a subheading")
st.button("Click Here", type="primary")
st.caption("This is used for caption")
st.button("This is the button")
st.checkbox("Click on the checkbox")
option=st.selectbox("Select from the options", items)
st.write(option," are the fruit that you have selected")
z=st.slider('z')
st.slider("Let's use it to print exponential value",z*z, 1,100)
st.slider("WE use Slider", 0 , 100 , (20,80))
string_value = st.text_input("Enter a string:", value="Hello, Streamlit!")
st.write(f"The string you entered is: {string_value}")
