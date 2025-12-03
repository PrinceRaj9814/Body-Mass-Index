
import streamlit as st

weight = st.number_input("Enter in m ")
height = st.number_input("Enter in kg ")

if st.button('calculate'):
    bmi = weight / (height ** 2)
    st.write(bmi)
