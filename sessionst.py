import streamlit as st

st.title("Simple Counter")

#initialize Counter

if "counter" not in st.session_state:
    st.session_state.counter = 0

#Buttons to interact with the counter
increment = st.button("Increment")
reset = st.button("Reset")
decrement = st.button("Decrement")

print(increment)
print(reset)
print(decrement)

#Control structure to manage the counter
if increment:
    st.session_state.counter +=1

if reset:
    st.session_state.counter = 0

if decrement:
    st.session_state.counter -=1    

#Display the counter value
st.write(f"Current_counter value: {st.session_state.counter}")

