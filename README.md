# 🧠 Medical Image Classification for Disease Detection
CNN-based medical image classification system for pneumonia detection using chest X-ray images with data augmentation and evaluation metrics.

## 📌 Overview

This project implements a **Convolutional Neural Network (CNN)** from scratch to classify **Chest X-ray images** into:

* ✅ NORMAL
* 🦠 PNEUMONIA

The goal is to assist in **early disease detection** using deep learning techniques.

---

## 🚀 Key Features

* 🔹 CNN built **from scratch (no pretrained models)**
* 🔹 **Data Augmentation** for better generalization
* 🔹 **Training vs Validation Accuracy & Loss graphs**
* 🔹 **Confusion Matrix**
* 🔹 **Precision, Recall, F1 Score**
* 🔹 Works on real-world medical dataset

---

## 🗂️ Dataset

* Dataset: **Chest X-ray Pneumonia Dataset**
* Source: Kaggle
* Classes:

  * NORMAL
  * PNEUMONIA

⚠️ Dataset is not included due to size limitations.

---

## 🧠 Model Architecture

The CNN model consists of:

* Convolutional Layers (Feature Extraction)
* MaxPooling Layers (Dimensionality Reduction)
* Dense Layers (Decision Making)
* Dropout (Overfitting Prevention)

---

## ⚙️ Tech Stack

* Python 🐍
* TensorFlow / Keras 🤖
* OpenCV 👁️
* NumPy 🔢
* Matplotlib 📊
* Scikit-learn 📈

---

## 📊 Results

### 📈 Accuracy Graph

Shows how the model improves during training.

![Accuracy Graph](C:\Users\NITESH\OneDrive\Pictures\Screenshots)

---


### 📊 Confusion Matrix

Visual representation of model predictions.

Confusion Matrix:

[ [  24  600 ]  
 [   1 5215 ] ]

---

### 🎯 Performance Metrics

| Metric    | Score    |
| --------- | -------- |
| Accuracy  | ~90–95%  |
| Precision | High     |
| Recall    | High     |
| F1 Score  | Balanced |

---

## 📥 Trained Model

Due to size limitations, the trained model is hosted externally:

👉 **Download Model Here:**
(Paste your Google Drive link here)

---

## ▶️ How to Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Medical-Image-Classification-For-Disease-Detection.git
cd Medical-Image-Classification-For-Disease-Detection
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run Training

```bash
jupyter notebook notebooks/model_training.ipynb
```

---

### 4️⃣ Run Prediction

```bash
python src/predict.py
```

---

## 🧪 Sample Prediction Output

```plaintext
Raw Prediction: [[0.82]]
🦠 PNEUMONIA DETECTED
```

---

## 📁 Project Structure

```
Medical-Image-Classification/
│
├── notebooks/
│   └── model_training.ipynb
│
├── src/
│   └── predict.py
│
├── models/
│   └── (model link provided)
│
├── results/
│   ├── accuracy.png
│   ├── loss.png
│   └── confusion_matrix.png
│
├── requirements.txt
├── README.md
```

---

## 🧠 Key Learnings

* Understanding CNN architecture from scratch
* Working with real-world medical datasets
* Model evaluation using multiple metrics
* Handling overfitting using augmentation & dropout

---

## 🚀 Future Improvements

* 🔹 Deploy as a **web application (Streamlit)**
* 🔹 Add **Grad-CAM visualization**
* 🔹 Use larger datasets for better accuracy
* 🔹 Optimize model for real-time predictions

---

## 👨‍💻 Author

**Nitish Kumar Namdeo**
🎓 B.Tech IT Student
📍 India

---

## 💼 Resume Description (ATS-Friendly)

Developed a CNN-based medical image classification system for pneumonia detection using chest X-rays, achieving ~92% accuracy. Implemented data augmentation, evaluation metrics (precision, recall, F1-score), and visualization techniques for performance analysis.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
