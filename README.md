<div align="center">

# 💻 Laptop Price Predictor

### Predict Laptop Prices Using Machine Learning & XGBoost

![Python](https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-Regressor-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

A Machine Learning web application that predicts the estimated price of a laptop based on its hardware specifications using **XGBoost Regression**.

</div>

---

# ✨ Highlights

- 💻 Predict Laptop Prices in Seconds
- 🤖 XGBoost Regression Model
- 📊 Complete Data Analysis & Visualization
- ⚙️ Feature Engineering Pipeline
- 🎨 Modern Streamlit User Interface
- 🧠 Trained on Real Laptop Specifications
- 📦 Modular Python Project Structure

---

# 🎯 Problem Statement

Laptop prices depend on many hardware specifications such as RAM, Processor, GPU, Storage, Display, Battery, and many more.

This project uses Machine Learning to learn these relationships and accurately estimate the market price of a laptop.

---

# 🧠 Machine Learning Workflow

```text
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Exploratory Data Analysis
   │
   ▼
Feature Engineering
   │
   ▼
Model Training
   │
   ▼
Model Comparison
   │
   ▼
Best Model Selection
   │
   ▼
Streamlit Deployment
```

---

# 📂 Dataset Features

The dataset contains detailed laptop specifications including:

| Hardware | Features |
|----------|----------|
| 💻 Brand | Brand, Model |
| ⚙️ Processor | Brand, Model, Generation, Cores, Threads |
| 🎮 Graphics | GPU Brand, GPU Model, GPU Memory |
| 🧠 Memory | RAM Size, RAM Type, RAM Speed |
| 💾 Storage | Storage Type, Storage Capacity |
| 🖥 Display | Screen Size, Resolution, Refresh Rate, Panel Type |
| 🔋 Hardware | Battery, Weight, Webcam |
| 📡 Connectivity | WiFi, Bluetooth |
| 🔐 Extras | Fingerprint Sensor, Keyboard Backlit |

Target Variable

```
Laptop Price (₹)
```

---

# 📊 Exploratory Data Analysis

Performed detailed EDA using:

- 📈 Histograms
- 📉 Boxplots
- 📊 Correlation Matrix
- 🔥 Feature Correlation
- 📌 Scatter Plots
- 💰 Brand-wise Price Analysis
- 📦 Price Distribution

---

# ⚙️ Feature Engineering

The following preprocessing techniques were applied:

- Duplicate Removal
- One Hot Encoding
- Column Transformer Pipeline
- Resolution Extraction
- PPI (Pixels Per Inch) Calculation
- Train-Test Split
- Automatic Feature Transformation

---

# 🤖 Machine Learning Models

Several regression algorithms were trained and evaluated.

| Model | Status |
|------|--------|
| Linear Regression | ✅ |
| Decision Tree Regressor | ✅ |
| Random Forest Regressor | ✅ |
| Gradient Boosting Regressor | ✅ |
| Extra Trees Regressor | ✅ |
| ⭐ XGBoost Regressor | Final Model |

---

# 🚀 Technologies Used

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib

### Machine Learning

- Scikit-learn
- XGBoost

### Deployment

- Streamlit

---

# 📁 Project Structure

```text
Laptop_Price_Predictor
│
├── app.py
├── style.css
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── laptop_price_dataset_india.csv
│
├── model/
│   └── pipeline.pkl
│
├── notebook/
│   └── laptop.ipynb
│
└── utils/
    ├── feature_engineering.py
    ├── prediction.py
    └── __init__.py
```

---

# ⚡ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Laptop_Price_Predictor.git
```

Go to the project directory

```bash
cd Laptop_Price_Predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📝 How It Works

```
Select Laptop Specifications
            │
            ▼
Feature Engineering
            │
            ▼
Data Preprocessing
            │
            ▼
XGBoost Prediction
            │
            ▼
Estimated Laptop Price
```

---

# 🔮 Future Improvements

- 📈 Price Trend Prediction
- 🤖 Laptop Recommendation System
- 💰 Budget-Based Laptop Suggestions
- ☁️ Cloud Deployment
- 📱 Mobile Responsive UI
- 🔍 Similar Laptop Finder

---

# 👨‍💻 Author

**Shadab Saifi**

🎓 BCA Graduate  
🤖 Machine Learning & Generative AI Enthusiast  
🐍 Python Developer

---

<div align="center">

### ⭐ If you like this project, don't forget to star the repository!

Made with ❤️ using **Python • Streamlit • Scikit-learn • XGBoost**

</div>