import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.text('Hello World!')

#st write to format text
## double asteriks for bold
## before and after underscore for italics
st.write("Current address : **Minnesota, Shoreview,** _USA_" )

#Reading a dataset
df = pd.read_csv('/Users/avi/Downloads/covid_19_india.csv')
st.write(df)

##plots
fig, ax = plt.subplots()
ax.scatter(np.arange(5), np.arange(5)**2)
st.write(fig)

##Fetch documentation
st.write(st.write)

## Tile, header and sub-header
st.title('Introduction to Streamlit')
st.header('This is the header')
st.subheader('Sub-Header')

##Code
code = """
def my_code():
    print(Hello World!)"""
st.code(code,language='python')