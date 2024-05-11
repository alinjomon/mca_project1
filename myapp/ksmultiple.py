import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

# Load a pre-trained CNN model (ResNet-50)
base_model = ResNet50(weights='imagenet', include_top=False)

# Define a custom head for similarity computation
inputs = keras.Input(shape=(224, 224, 3))
x = base_model(inputs)
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dense(512, activation='relu')(x)
outputs = layers.Lambda(lambda x: tf.math.l2_normalize(x, axis=1))(x)  # L2 normalization
model = keras.Model(inputs, outputs)

# Load and preprocess dress images (replace these paths with your dataset)
top_dress_image_paths = ['top.jpeg', 'top2.jpeg', 'top3.jpeg', 'top4.jpeg']
bottom_dress_image_paths = ['btm.jpeg','btm2.jpeg','btm3.jpeg']


# Function to load and preprocess an image
def load_and_preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = preprocess_input(img)
    return img

# Extract features for all top and bottom dresses
top_dress_features = []
bottom_dress_features = []

for top_image_path in top_dress_image_paths:
    top_dress_img = load_and_preprocess_image(top_image_path)
    top_dress_features.append(model.predict(np.expand_dims(top_dress_img, axis=0)))

for bottom_image_path in bottom_dress_image_paths:
    bottom_dress_img = load_and_preprocess_image(bottom_image_path)
    bottom_dress_features.append(model.predict(np.expand_dims(bottom_dress_img, axis=0)))

# Calculate cosine similarity between all pairs of top and bottom dresses
similarities = np.dot(np.vstack(top_dress_features), np.vstack(bottom_dress_features).T)

# Display the similarity matrix
print("Similarity Matrix:")
print(similarities)

# You can set a threshold to determine if the dresses match or not
threshold = 0.6 # Adjust this threshold as needed

# Find and display matching combinations
for i, top_similarities in enumerate(similarities):
    matching_bottom_indices = np.where(top_similarities >= threshold)[0]
    if matching_bottom_indices.any():
        print(f"Top Dress {i + 1} matches with Bottom Dress(es): {matching_bottom_indices + 1}")
    else:
        print(f"No matching Bottom Dress found for Top Dress {i + 1}")