import streamlit as st
import pandas as pd
import numpy as np
import time


st.title('Session4 - Streamlit Buttons and Widgets')
#st.write(time.time())
#pr = st.button('Click Me!')
#st.write(pr)

pr = st.button('Here!')
if pr == True:
    st.write(time.time())


def fn():
    st.write(time.time())
st.button('Click Me!', on_click=fn)

##Download
df = pd.DataFrame(np.random.randn(10,2),columns=['col1','col2'])
data = df.to_csv().encode('utf-8')
st.download_button(
    label='Download file',
    data = data,
    file_name = 'my_exp.csv')

text = "This is a text"
st.download_button(
    label = 'Download- Click here',
    data = text,
    file_name = 'my_file.txt'
)

file = open('/Users/avi/Downloads/Sam_ALtman.jpeg', 'rb')
btn = st.download_button(
    label = 'Download image',
    data = file,
    file_name = 'Sam_Altman.jpg',
    mime= 'image/jpg'
)

##Checkbox
st.subheader('This is checkbox')
cb = st.checkbox('I agree!', value=True)
if cb == True:
    st.write('I understand')
else:
    st.write('Get the hell out of here!')

##Radiobuttons
st.subheader('This is radio button')
radio = st.radio(
    label = 'Choose your main subject',
    options = ['Physics','Mathematics','Biology'],
    index = 0
)
if radio == 'Mathematics':
    st.write('Maths is my subject')
else:
    st.write("I don't care!")

##Selectbox
st.subheader('This is select box')
box = st.selectbox(
    label = 'Where do you live?',
    options = ['USA','Finalnd','Georgia'],
    index = 0
)
if box == 'USA':
    st.write('I live in USA')
else:
    st.write("I don't care!")