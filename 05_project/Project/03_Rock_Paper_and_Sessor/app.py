import random   
import streamlit as st
st.title("Rock, Paper, Sessor")
items = ['rock', 'paper', 'sessior']
choice = random.choice(items)

user_choice = st.selectbox('Choose your weapon', items)

if user_choice == choice:
    st.warning("It's a tie")
elif user_choice == 'rock' and choice == 'sessior':
    st.success("You win")

elif user_choice == 'rock' and choice == 'paper':
    st.error("You lose")

elif user_choice == 'sessior' and choice == 'rock':
    st.error("You lose")

elif user_choice == 'sessior' and choice == 'paper':
    st.success("You win")

elif user_choice == 'paper' and choice == 'rock':
    st.success("You win")

elif user_choice == 'paper' and choice == 'sessior':
    st.error("You lose")
else:
    st.write("Invalid input")

st.write(f"your opponenet choose :red[{choice}]")