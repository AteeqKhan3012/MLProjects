import streamlit as st
import random

counter=1
while True:

    num=random.randint(1,10)

    temp=st.number_input("Enter any number",min_value=1,max_value=10,step=1)

    if num==temp:
        st.write("You win!!!")
        break
    
    if counter==6:
        st.write("Max Try over!!!")
        break
    
    counter=counter+1
print("Game Over")    