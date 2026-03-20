import numpy as np
import cv2
import os
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("models/medical_cnn_model.h5")

# Path to test image (change this)
img_path = "test_image.jpeg"

# Check if file exists
if not os.path.exists(img_path):
    print("❌ Image not found. Please check path.")
else:
    img = cv2.imread(img_path)

    if img is None:
        print("❌ Error loading image.")
    else:
        # Resize image
        img = cv2.resize(img, (128,128))

        # Normalize
        img = img / 255.0

        # Reshape
        img = np.reshape(img, (1,128,128,3))

        # Predict
        prediction = model.predict(img)

        print("Raw Prediction:", prediction)

        if prediction > 0.5:
            print("🦠 PNEUMONIA DETECTED")
        else:
            print("✅ NORMAL")
