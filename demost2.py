import streamlit as st

option = st.selectbox(
"How would you like to be contacted?",
("Email", "Home phone", "Mobile phone"),
placeholder="Select contact method...")
st.write("You selected:", option)
