# Football Players Analyser

**Author:** Kshitij Sandeep Shroff

---

## 📌 Project Overview

**Football Players Analyser** is a portfolio-grade machine learning project built on the FIFA 21 complete player dataset. The project combines predictive modeling with an interactive Streamlit application to analyze football players from both **sporting** and **commercial** perspectives.

The system is designed to demonstrate practical ML workflows, feature engineering, and user-facing data applications.

---

## 🚀 Key Features

### 1️⃣ Player Prediction App

* Predicts a player’s:

  * **Market Value**
  * **Overall Rating**
  * **Potential Rating**
* Uses technical and physical attributes such as pace, shooting, passing, dribbling, defending, and physicality

#### 🔹 Augmented Predictor

* Extends traditional performance-based prediction
* Incorporates **commercial popularity** (e.g., Instagram followers)
* Allows users to adjust a **Fame slider** to see how off-field popularity impacts market valuation

---

### 2️⃣ Football Chatbot

* Built using **Streamlit**
* Supports **natural language queries** about players and clubs
* Example queries:

  * `Messi stats`
  * `top players for pace`
  * `random player`

#### 🎙️ Voice Interaction

* Speech-to-text input using **SpeechRecognition**
* Text-to-speech responses using **gTTS**
* Enables hands-free conversational interaction

---

## 🧠 Dataset

* **FIFA 21 Complete Player Dataset**
* ~19,000 players
* 100+ attributes per player
* Augmented with synthetic social media metrics for commercial value analysis

Dataset source:
[https://www.kaggle.com/datasets/stefanoleone992/fifa-21-complete-player-dataset](https://www.kaggle.com/datasets/stefanoleone992/fifa-21-complete-player-dataset)

---

## ⚙️ Installation

### Environment

* **Python 3.12.x** (recommended)
* Use a virtual environment for audio library compatibility

### Required Packages

```bash
pip install pandas numpy matplotlib scikit-learn streamlit \
            SpeechRecognition PyAudio gTTS joblib
```

---

## ▶️ Usage

### 🔹 Run the Prediction App

```bash
streamlit run home.py
```

You will land on the home page of the project and from there you
can navigate on to all the different pages of the project including the prediction page, chatbot etc.

---

### 🔹 Train Models (Optional)

Models are **not included** in the repository to keep it lightweight and reproducible.

```bash
python train_classifier.py
python train_feasibility.py
python train_augmented_model.py
```

Trained models will be saved locally in the `models/` directory.

---

### 🔹 Run the Football Chatbot

```bash
streamlit run app.py
```

* Supports both text and voice-based interaction
* Responses are displayed on-screen and can also be spoken aloud

---

## 📁 Project Structure

```
Machine-Learning---Prediction/
│
├── pages/
│   └── Transfer_Scout.py
├── train_classifier.py
├── train_feasibility.py
├── train_augmented_model.py
├── data/          # dataset (not tracked)
├── models/        # trained models (not tracked)
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Motivation

This project demonstrates how machine learning models can be combined with interactive applications to deliver real-world insights. It highlights the impact of both **on-pitch performance** and **off-field popularity** on player valuation, while also showcasing natural language interfaces for sports analytics.

---

## Contact

Feel free to connect with me on GitHub or LinkedIn for feedback, collaboration, or discussion around machine learning and sports analytics.
