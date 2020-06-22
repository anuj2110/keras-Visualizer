# Core Pkgs
import streamlit as st 

# EDA Pkgs
from tensorflow.keras.applications import VGG16
import numpy as np 
from PIL import Image

# Data Viz Pkg
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")




def main():
    st.title("Keras Visualizer")
    activities = ["NONE","CNN","LSTM"]
    choice=st.sidebar.selectbox(label="Select an NN type",options=activities)

    if choice=="NONE":
        st.subheader("\n\n\nPlease select an NN architecture to visualize")
    elif choice=="CNN":
        st.subheader("CNN Visualizer")
        image = st.file_uploader(label = "",type=["png","jpg","jpeg"])
        img = None
        if image is not None:
            img = Image.open(image)
            st.image(img,width=int(img.width/2))
            
    


if __name__ == '__main__':
	main()