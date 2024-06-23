import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

st.title('Session2 - Streamlit data')
## dataframe, metric, table, json

names = ['avi','ron','som','san','arb']
marks = [12,15,45,43,32]
data = list(zip(names, marks))

# Create the DataFrame
df = pd.DataFrame(data, columns=['names', 'marks'])

st.write(df)

st.dataframe(np.random.randn(5,5))

## table
st.table(df)

##metric
st.metric("TCS", value="3780.35", delta="23.40", delta_color='inverse')

##json
file = open("/Users/avi/Downloads/my_json.json")
df_json = json.load(file)
#True to expand and False to collapse the json
st.json(df_json,expanded = False)
