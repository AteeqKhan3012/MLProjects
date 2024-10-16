import streamlit as st
import random

num=random.randint(1,10)
st.title("Guessing Game")

st.write("Guess a number between 1 and 100")

temp=st.number_input("Enter any number",min_value=1,max_value=10,step=1,key="key1")

print(temp)

if num==temp:
    st.write("You guessed it right!!")
else:
    st.write("You guessed it wrong, try again!!")
