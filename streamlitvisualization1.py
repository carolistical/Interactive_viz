import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import io
#creating a header
st.header("Scatter plot Weight VS dog intelligence")
#reading the csv
dog_intelligence = pd.read_csv("https://raw.githubusercontent.com/carolistical/Visualization1-scatterplot/main/intelligence.csv")
#creating an if statement to show the data
if st.checkbox("Show data"):
    dog_intelligence
#creating an box select for x and y axis
x_axis = st.selectbox('Select X-axis', options =['height_high_inches','average_weight'])
y_axis = st.selectbox('Select Y-axis', options =['average_reps_to_learn_something'])

#creating the scatter and linking it to box select for interactivity
Scatter =  px.scatter(dog_intelligence, x = x_axis, y = y_axis, title="Weight Vs Intelligence", size = y_axis, color = 'Breed')

#download the png of the scatterplot (not coloured)
if st.checkbox("Create Scatterplot for data"):
    st.plotly_chart(Scatter)
    buffer = io.BytesIO()
    Scatter.write_image(buffer, format='png')
    buffer.seek(0)
    st.download_button(label='Download Scatterplot Image', data=buffer, file_name='scatterplot.png',key='scatterplot_image')
