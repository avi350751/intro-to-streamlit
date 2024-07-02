import streamlit as st
import pandas as pd
import numpy as np
from datetime import time


st.title('Session5 - Streamlit Buttons and Widgets-Continue')
st.subheader('This is multiselect!')

option = st.multiselect(
    label = "Which places you have been?",
    options = ('Durgapur','Jaipur','Dispur','Raghunathpur','Nagpur'),
    default = ('Durgapur')
)
st.write(option)


st.subheader('This is slider!')

num = st.slider(
    label = "What is your age?",
    min_value = 1,
    max_value= 100,
    value = 20,
    step = 1
)

st.write(num)


age = st.slider(
    label = "What is your age?",
    min_value = 1,
    max_value= 100,
    value = (20,60),
    step = 1
)

st.write(age)

visit_time = st.slider(
    label = "When is your appintment?",
    value = (time(11,15), time(12,45))
)

st.write(visit_time)

st.subheader('This is select slider')
color = st.select_slider(
    label = "which color?",
    options = ('red','blue','green','indigo','orange')
)

st.write(color)


start_color , end_color = st.select_slider(
    label = "which color?",
    options = ('red','blue','green','indigo','orange'),
    value=('blue','indigo')
)

st.write("From",start_color,"To",end_color)


st.subheader('This is text input')
email = st.text_input(
    label = "Enter your email address",
    placeholder = 'Email',
    max_chars = 30
)

st.write(email)

pwd = st.text_input(
    label = "Enter your password",
    placeholder = 'Password',
    max_chars = 20,
    type = "password"
)

st.write(pwd)


st.subheader('This is number input')
num_input = st.number_input(
    label = "Enter your weight",
    min_value = 20,
    max_value = 120,
    value =68,
    step = 1
)
st.write(num_input)