# Handwritten Digit Recognition using CNN

## Overview
This project implements a **Handwritten Digit Recognition system** using a **Convolutional Neural Network (CNN)**.  
The model is trained on the **MNIST dataset** to classify handwritten digits from **0–9**.  
A simple **Streamlit web interface** is used to interact with the trained model and make predictions.

---

## Technologies Used
- Python
- TensorFlow / Keras
- Convolutional Neural Networks (CNN)
- NumPy
- Matplotlib
- Streamlit

---

## Dataset
This project uses the **MNIST dataset**, which contains images of handwritten digits.

Dataset details:

- Total images: 70,000
- Training images: 60,000
- Testing images: 10,000
- Image size: 28 × 28 pixels
- Classes: Digits from 0 to 9

The dataset is automatically downloaded using TensorFlow.

```python
tf.keras.datasets.mnist.load_data()
