import os
import pickle
import numpy as np
import random
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.models import Sequential

from utils.helper import recommend, detect_color, detect_clothing_type


app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Allowed image formats
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

# Load Deep Learning Model
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224,224,3))
base_model.trainable = False

model = Sequential([
    base_model,
    GlobalMaxPooling2D()
])

# Load extracted features
feature_list = pickle.load(open("features/feature_list.pkl","rb"))
filenames = pickle.load(open("features/filenames.pkl","rb"))


# Check file extension
def allowed_file(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS


# Feature Extraction
def extract_features(img_path):

    img = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    result = model.predict(img_array, verbose=0).flatten()

    # Normalize vector safely
    norm = np.linalg.norm(result)
    if norm == 0:
        return result
    return result / norm


@app.route("/", methods=["GET","POST"])
def index():

    if request.method == "POST":

        file = request.files["file"]

        if file.filename == "":
            return render_template("index.html")

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

            upload_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(upload_path)

            # Extract features
            features = extract_features(upload_path)

            # Get recommendations
            indices, scores = recommend(features, feature_list)

            # Detect color
            detected_color = detect_color(upload_path)

            # Detect clothing type
            clothing_type = detect_clothing_type(upload_path)

            recommended_images = []
            similarity_scores = []
            product_names = []
            categories = []
            brands = []

            brands_list = ["Nike","Adidas","Puma","Zara","H&M","Levis"]

            for i, score in zip(indices, scores):

                filename = os.path.basename(filenames[i])
                recommended_images.append("images/" + filename)

                similarity_scores.append(round(score * 100,2))

                product_id = filename.split(".")[0]
                product_names.append("Fashion Product " + product_id)

                name_lower = filename.lower()

                if "shoe" in name_lower or "sneaker" in name_lower:
                    categories.append("Shoes")

                elif "shirt" in name_lower:
                    categories.append("Shirt")

                elif "tshirt" in name_lower or "t-shirt" in name_lower:
                    categories.append("T-Shirt")

                elif "jacket" in name_lower:
                    categories.append("Jacket")

                elif "hoodie" in name_lower:
                    categories.append("Hoodie")

                else:
                    categories.append(clothing_type)

                brands.append(random.choice(brands_list))


            return render_template(
                "index.html",
                uploaded="uploads/" + file.filename,
                recommendations=recommended_images,
                scores=similarity_scores,
                detected_color=detected_color,
                clothing_type=clothing_type,
                product_names=product_names,
                categories=categories,
                brands=brands
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)