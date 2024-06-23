import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('Session3 - Streamlit Plot and Charts')
df = pd.DataFrame(np.random.randn(5,2), columns=['prices','diff'])
st.write(df)

st.markdown('Line Chart')
## Line chart
st.line_chart(df)

## Line chart- Only one
st.line_chart(df, y = ["prices"])

st.markdown('Area Chart')
## Area chart
st.area_chart(df)

st.markdown('Bar Chart\n')
# Bar Chart
st.bar_chart(df)

##bar Chart - only one
st.bar_chart(df,y=['prices'])

##Matplotlib
st.markdown('Scatter plot')
fig, ax = plt.subplots()
ax.scatter(np.arange(10) , np.arange(10)**2)
st.pyplot(fig)

##Histogram
st.markdown('Histogram')
fig1,ax= plt.subplots()
ax.hist(np.random.randn(100),bins=10)
st.pyplot(fig1)

##Map
st.markdown('Map')
places = pd.DataFrame({
    "lat" : [19.63, 20.64],
    "lon" :[72.65, 80.65]
})
st.map(places)