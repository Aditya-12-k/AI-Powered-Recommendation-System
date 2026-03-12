import os
import numpy as np
import pickle
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.models import Sequential
from tqdm import tqdm

model = Sequential([
    ResNet50(weights='imagenet', include_top=False, input_shape=(224,224,3)),
    GlobalMaxPooling2D()
])

dataset_path = "dataset/images"

feature_list = []
filenames = []

for file in tqdm(os.listdir(dataset_path)):

    img_path = os.path.join(dataset_path, file)

    img = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    result = model.predict(img_array).flatten()

    feature_list.append(result)
    filenames.append(img_path)

pickle.dump(feature_list, open("features/feature_list.pkl","wb"))
pickle.dump(filenames, open("features/filenames.pkl","wb"))