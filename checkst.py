import streamlit as st

st.title("Boolean Example")

# Boolean value
is_active = st.checkbox("Is active?", value=True)
st.checkbox("hello")
# Display the bo"olean value
st.write(f"Is active: {is_active}")
