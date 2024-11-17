import streamlit as st
import streamlit.components.v1 as components

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


import numpy as np
import shutil
import tensorflow as tf

import os # inbuilt module
import random # inbuilt module
import webbrowser # inbuilt module

st.header(':orange[M-Stock:] Automate Photo Assessment for Enhancing Student Photography Skills with Deep Learning', divider='rainbow')
st.write("*Authors: Mr.Nontawat Thongsibsong, Assistant Professor Dr.Surapol Vorapatratorn*")
st.write("*Center of Excellence in AI and Emerging Technology | Mae Fah Luang University 2024*")
import streamlit as st

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7, col8, col9 = st.columns(3)
col10,col11, col12 = st.columns(3)

with col1:
	with st.container(border=1):
		st.write("**Fast Shutter Speed**")
		st.image('./image/p1.jpg')
		st.write("*Capture split-second moments with precision and clarity using fast shutter speeds.*")
		submit1 = st.button('Start 🤾')
with col2:
	with st.container(border=1):
		st.write("**Long Shutter Speed**")
		st.image('./image/p2.jpg')
		st.write("*Transform time into art with long exposure photography, creating ethereal scenes and light trails.*")
		submit2 = st.button('Start 🎆')
with col3:
	with st.container(border=1):
		st.write("**Night Light Photography**")
		st.image('./image/p3.jpg')
		st.write("*Explore the beauty of low-light environments.*")
		submit3 = st.button('Start 🌛')
with col4:
	with st.container(border=1):
		st.write("**Composition and Subject**")
		st.image('./image/p4.jpg')
		st.write("*Master the fundamentals of composition to create visually compelling images that tell a story.*")
		submit4 = st.button('Start 🏕️')
with col5:
	with st.container(border=1):
		st.write("**Aperture & Depth of Field**")
		st.image('./image/p5.jpg')
		st.write("*Control focus and create visual impact with aperture settings to manipulate depth of field.*")
		submit5 = st.button('Start 🏞️')
with col6:
	with st.container(border=1):
		st.write("**Light and Shadow**")
		st.image('./image/p6.jpg')
		st.write("*Sculpt form and mood in your photographs using the interplay of light and shadow.*")
		submit6 = st.button('Start 💡')
with col7:
	with st.container(border=1):
		st.write("**Portrait Photography**")
		st.image('./image/p7.jpg')
		st.write("*Capture the essence of your subjects with carefully crafted compositions and lighting.*")
		submit7 = st.button('Start 👩')
with col8:
	with st.container(border=1):
		st.write("**Moving Subject**")
		st.image('./image/p8.jpg')
		st.write("*Shooting subjects against a moving background using the pan technique.*")
		submit8= st.button('Start 🏍️')
with col9:
	with st.container(border=1):
		st.write("**Product Photography**")
		st.image('./image/p9.jpg')
		st.write("*Showcase merchandise in its best light through skillful styling, lighting, and composition.*")
		submit9 = st.button('Start 🍮')
with col10:
	with st.container(border=1):
		st.write("**Shutterstock Project**")
		st.image('./image/p10.jpg')
		st.write("*Collaborate on a real-world photography project to curate a collection of images for commercial licensing.*")
		submit10 = st.button('Start ☁️')
if submit1:
	st.switch_page("./pages/1_🤾_Fast Shutter Speed.py")
elif submit2:
	st.switch_page("./pages/2_🎆_Long Shutter Speed.py")
elif submit3:
	st.switch_page("./pages/3_🌛_Night Light Photography.py")
elif submit4:
	st.switch_page("./pages/4_🏕️_Composition and Subject.py")
elif submit5:
	st.switch_page("./pages/5_🏞️_Aperture & Depth of Field.py")
elif submit6:
	st.switch_page("./pages/6_💡_Light and Shadow.py")
elif submit7:
	st.switch_page("./pages/7_👩_Portrait Photography.py")
elif submit8:
	st.switch_page("./pages/8_🏍️_Moving Subject.py")
elif submit9:
	st.switch_page("./pages/9_🍮_Product Photography.py")
elif submit10:
	st.switch_page("./pages/10_☁️ _Shutterstock Project.py")

st.write("*Copyright © Center of Excellence in AI and Emerging Technology | Mae Fah Luang University 2024*")
