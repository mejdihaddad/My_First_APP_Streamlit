from matplotlib import image
import streamlit as st
import plotly.express as px
import pandas as pd
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "image", "image.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "flipkart_smartphones.csv")
st.title("Dashboard - Flipkart Smartphones")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

models = st.selectbox("Select the Model:", df['model'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['model'] == models], x="ratings")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['model'] == models], y="reviews")
col2.plotly_chart(fig_2, use_container_width=True)
