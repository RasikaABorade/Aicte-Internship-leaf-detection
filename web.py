import streamlit as st
import tensorflow as tf
import numpy as np

def model_prediction(test_image):
    model=tf.keras.models.load_image("trained_plant_disease_model.keras")
    image=tf.keras.preprocessing.image.load_img(test_image,target_size(128,128))
    