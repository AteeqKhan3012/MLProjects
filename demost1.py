import streamlit as st

st.title("List example")

#List of items
items = ["apple", "Banana", "cherry", "Dates"]

#Select item from list
selected_item = st.selectbox("Select a fruit:",items)

#Display the selected item
st.write(f"You selected:{selected_item}")