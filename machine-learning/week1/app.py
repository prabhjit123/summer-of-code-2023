import streamlit as st
import pickle
import pandas as pd
import numpy as np
#importing the model
pipelines = pd.read_pickle('pipe.pkl')
smartphone = pd.read_pickle('smartphones.pkl')
st.title("Smartphone predictor")
#Allows user to selct a brand
company = st.selectbox('Brand', smartphone['brand'].unique())
#Allows user to select batter_type
battery_type = st.selectbox('Battery',smartphone['battery_type'].unique())
memory = st.number_input("Memory")
storage = st.number_input('Storage')
front_camera = st.number_input("Front Camera")
rear_camera = st.number_input("Rear Camera")
display_size = st.number_input("Display Size (Inches)")
battery_capacity = st.number_input("battery capacity")
if st.button('Predict Price'):
    query = pd.DataFrame({
        'brand': [company],
        'memory': [memory],
        'storage': [storage],
        'rear_camera': [rear_camera],
        'display_size': [display_size],
        'battery_capacity': [battery_capacity],
        'battery_type': [battery_type],
        'front_camera': [front_camera]
    })
    st.title(pipelines.predict(query))
