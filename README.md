# 👕 Fashion Recommendation System using Deep Learning

A Deep Learning-based Fashion Recommendation System that recommends visually similar fashion products based on an uploaded image. The system extracts image features using a pre-trained Convolutional Neural Network (CNN) and recommends the most similar fashion items using feature similarity.

---

# 📌 Project Overview

Finding fashion products similar to a user's preferred style can be time-consuming. This project leverages **Deep Learning** and **Computer Vision** techniques to recommend visually similar fashion items from a product catalog.

The application extracts feature vectors from product images using a pre-trained CNN model and compares them using similarity metrics to generate accurate recommendations.

---

# 🚀 Features

- 👕 Upload a fashion product image
- 🧠 Deep Learning-based feature extraction
- 📸 Image similarity search
- 🎯 Top similar fashion recommendations
- 🌐 User-friendly Flask web application
- ⚡ Fast recommendation system
- 📂 Easy-to-use interface

---

# 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- Flask
- NumPy
- Scikit-learn
- OpenCV
- Pillow (PIL)
- Pickle
- HTML
- CSS

---

# 📂 Project Structure

```text
Fashion-Recommendation-System/
│
├── features/               # Extracted image feature vectors
├── static/                 # CSS, JavaScript, Images
├── templates/              # HTML templates
├── uploads/                # Uploaded user images
├── utils/                  # Utility functions
│
├── app.py                  # Flask application
├── train_model.py          # Feature extraction script
├── requirements.txt        # Project dependencies
├── .gitignore
└── README.md
```

---

# 🧠 Deep Learning Model

The project uses a **pre-trained Convolutional Neural Network (CNN)** for feature extraction.

### Workflow

- Upload an image
- Preprocess the image
- Extract deep feature vectors using CNN
- Normalize feature vectors
- Calculate similarity using Nearest Neighbors
- Display the most similar fashion products

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Aditya-12-k/Fashion-Recommendation-System.git
```

## 2. Navigate to the Project Folder

```bash
cd Fashion-Recommendation-System
```

## 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

## 4. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

# 🔄 System Workflow

1. Load the image dataset.
2. Extract deep image features using a pre-trained CNN.
3. Store feature vectors.
4. Upload a query image.
5. Extract features from the uploaded image.
6. Compare features using Nearest Neighbors.
7. Recommend the most visually similar fashion products.

---

# 📊 Recommendation Technique

- Deep Feature Extraction
- Transfer Learning
- Euclidean Distance
- Nearest Neighbors Algorithm

---



# 📦 Requirements

Install all required packages using:

```bash
pip install -r requirements.txt
```

Major libraries:

- TensorFlow
- Keras
- Flask
- NumPy
- Scikit-learn
- OpenCV
- Pillow

---

# 🔮 Future Improvements

- User Authentication
- Personalized Fashion Recommendations
- Color-Based Search
- Multi-Image Recommendation
- Mobile Application
- Deploy on AWS, Render, or Railway
- Real-Time Recommendation API

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---


---

⭐ If you found this project useful, please consider giving it a **Star ⭐** on GitHub!
