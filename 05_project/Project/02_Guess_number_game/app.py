import streamlit as st
user = 12
st.title("Guess the number")

user_guess = st.number_input("Guess a number between 1 and 10")
if user_guess == user:
    st.write("You got it!")
elif user_guess < user:
    st.write("Too low")
elif user_guess > user:
    st.write("Too high")
else:
    st.write("Invalid input")
st.write(f"The correct number was {user}")