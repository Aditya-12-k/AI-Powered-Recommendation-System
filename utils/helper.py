import numpy as np
import cv2
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image


# Load AI Model for clothing detection
clothing_model = ResNet50(weights="imagenet")


# Recommendation Function
def recommend(features, feature_list):

    similarity = cosine_similarity([features], feature_list)[0]

    indices = np.argsort(similarity)[-6:-1][::-1]

    scores = similarity[indices]

    return indices, scores


# Improved Color Detection
def detect_color(img_path):

    img = cv2.imread(img_path)

    if img is None:
        return "Unknown"

    img = cv2.resize(img, (200,200))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    pixels = img.reshape((-1,3))

    kmeans = KMeans(n_clusters=3, random_state=0)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_

    dominant_color = colors[0]

    r,g,b = dominant_color

    if r > 200 and g > 200 and b > 200:
        return "White"
    elif r > 150 and g < 100 and b < 100:
        return "Red"
    elif b > 150 and g < 120:
        return "Blue"
    elif g > 150 and r < 120:
        return "Green"
    elif r > 150 and g > 150:
        return "Yellow"
    elif r < 80 and g < 80 and b < 80:
        return "Black"
    else:
        return "Mixed Color"


# REAL AI Clothing Type Detection
def detect_clothing_type(img_path):

    img = image.load_img(img_path, target_size=(224,224))

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)

    img_array = preprocess_input(img_array)

    preds = clothing_model.predict(img_array)

    decoded = decode_predictions(preds, top=1)[0][0][1]

    label = decoded.lower()

    # Map ImageNet labels to clothing types
    if "shoe" in label or "sneaker" in label:
        return "Shoes"

    elif "jersey" in label or "tshirt" in label:
        return "T-Shirt"

    elif "jacket" in label:
        return "Jacket"

    elif "coat" in label:
        return "Coat"

    elif "jean" in label:
        return "Jeans"

    else:
        return "Fashion Item"