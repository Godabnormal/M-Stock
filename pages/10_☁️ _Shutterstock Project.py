import streamlit as st

from PIL import Image
from tensorflow.keras.preprocessing.image import load_img, img_to_array, save_img
from tensorflow.keras.models import model_from_json
import numpy as np

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import plot_model
from tensorflow.keras.models import model_from_json
import pickle as p
from tensorflow.keras import layers
to_categorical = tf.keras.utils.to_categorical

import shutil

chapter = "ShutterStockProject"

import numpy as np
import shutil
import tensorflow as tf

import os # inbuilt module
import random # inbuilt module
import webbrowser # inbuilt module

st.header(':orange[M-Stock:] Automate Photo Assessment for Enhancing Student Photography Skills with Deep Learning', divider='rainbow')
st.write("### ☁️ Shutter Stock Project")
st.write("Collaborate on a real-world photography project to curate a collection of images for commercial licensing.")
st.image('./image/p10.jpg')


#==================================== Model ==================================
def processing(testing_image_path):
	img_height = 800
	img_width = 800
	test_path = (testing_image_path)
	img = load_img(test_path, target_size=(img_height, img_width))
	img_array = img_to_array(img)
	img_array = tf.expand_dims(img_array, 0)
	prediction =loaded_model.predict(img_array)
	return prediction

def generate_result(prediction, testing_image_name):
	test_name = (testing_image_name)
	class_names = ['Accepted', 'Rejected']
	score = tf.nn.softmax(prediction[0])
	print("Result is {}, Prediction Score {:.2f}%" .format(class_names[np.argmax(score)],100*np.max(score)))
	if np.argmax(score)==0:
		st.write("## 🎯 Result is :green[{}] 👏" .format(class_names[np.argmax(score)]))
		save_img("E:/Jupyter/temp_dir/"+str(chapter)+"/Accepted/"+str(test_name), img_array)
	else:
		st.write("## 🎯 Result is :red[{}] 👎" .format(class_names[np.argmax(score)]))
		save_img("E:/Jupyter/temp_dir/"+str(chapter)+"/Rejected/"+str(test_name), img_array)
	st.write("Prediction Score: {:.2f}%" .format(100*np.max(score)))


#========================== File Uploader ===================================
img_file_buffer = st.file_uploader("Upload an image here👇🏻",)

try:
	image = Image.open(img_file_buffer)
	image_name = img_file_buffer.name
	img_array = np.array(image)
	if image is not None:
		try:
			save_img("temp_dir/"+str(chapter)+"/test_image.png", img_array)

			image_path = "temp_dir/"+str(chapter)+"/test_image.png"
			# Predicting

			model_path_h5 = "model/"+str(chapter)+"/model.h5"
			model_path_json = "model/"+str(chapter)+"/model.json"
			json_file = open(model_path_json, 'r')
			loaded_model_json = json_file.read()
			json_file.close()
			loaded_model = model_from_json(loaded_model_json)
			loaded_model.load_weights(model_path_h5)

			loaded_model.compile(loss='binary_crossentropy', metrics=['accuracy'],optimizer='adam')

			prediction = processing(image_path)
			generate_result(prediction, image_name)
			st.image(image, use_column_width=True)
			st.write("*Copyright © Center of Excellence in AI and Emerging Technology | Mae Fah Luang University 2024*")
		except:
			st.write("""
			#### ❗ Oops... Something Is Going Wrong
				""")
except:
	st.write("""
		#### ❗ Any Picture hasn't selected yet!!!
		""")