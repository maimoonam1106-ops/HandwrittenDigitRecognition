import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# Load trained model
model = tf.keras.models.load_model("digit_model.h5")

st.title("Handwritten Digit Recognition")

uploaded_file = st.file_uploader("Upload a digit image", type=["png","jpg","jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")
    image = image.resize((28,28))
    
    img = np.array(image)
    img = img / 255.0
    img = img.reshape(1,28,28,1)

    prediction = model.predict(img)
    digit = np.argmax(prediction)

    st.image(image, caption="Uploaded Image", width=150)
    st.write("### Predicted Digit:", digit)