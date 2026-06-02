import streamlit as st

st.title("Welcome to this demo app!")

st.header("This is a simple calculator")

def sqr(num):
    return num*num

num = st.number_input("Insert a number", value=0)

if st.button("Submit"):
    result = sqr(num)
    st.write(f"The square of {num} is {result}")



