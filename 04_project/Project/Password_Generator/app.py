import streamlit as st
import random

password_length = st.slider("Select the length of your password", min_value=8, max_value=10000000000, value=12, step=1)

password = ""
for i in range(password_length):
    password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")


st.write("Your generated password is: ", password)

