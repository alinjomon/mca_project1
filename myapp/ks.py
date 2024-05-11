
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
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
top_dress_image_path = 'D:\\bertsentiment\\img\\top.jpeg'
bottom_dress_image_path = 'D:\\bertsentiment\\img\\btm2.jpeg'

# Load and preprocess images
def load_and_preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = preprocess_input(img)
    return img

top_dress_img = load_and_preprocess_image(top_dress_image_path)
bottom_dress_img = load_and_preprocess_image(bottom_dress_image_path)

# Extract features for the dresses
top_dress_features = model.predict(np.expand_dims(top_dress_img, axis=0))
bottom_dress_features = model.predict(np.expand_dims(bottom_dress_img, axis=0))

# Calculate cosine similarity between the features
similarity = np.dot(top_dress_features, bottom_dress_features.T)

# Display the similarity score
print(f"Similarity score: {similarity[0][0]}")

# You can set a threshold to determine if the dresses match or not
threshold = 0.8  # Adjust this threshold as needed
if similarity[0][0] >= threshold:
    print("The dresses are matching!")
else:
    print("The dresses do not match.")