import streamlit as st
import random

comp = random.randint(1,10)
st.title("Guess the number")

user_guess = st.number_input("Guess a number between 1 and 10")
if user_guess == comp:
    st.write("You got it!")
elif user_guess < comp:
    st.write("Too low")
elif user_guess > comp:
    st.write("Too high")
else:
    st.write("Invalid input")
st.write(f"The correct number was {comp}")