
# HeartCare - Heart Disease Classification

**HeartCare** is a machine learning project aimed at predicting heart diseases based on medical data. The app leverages various machine learning models to classify whether a person has heart disease or not, based on input features like age, blood pressure, cholesterol levels, etc.

🧠 **Live App**: [https://heartdeseas-rj.streamlit.app/](https://heartdeseas-rj.streamlit.app/)  
📊 **Dataset Source**: [Kaggle - Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Models Used](#models-used)
- [How to Run Locally](#how-to-run-locally)
- [File Structure](#file-structure)
- [Collaborators](#collaborators)
- [License](#license)

## Project Overview

This project is a heart disease classification app built using **Streamlit** for the front-end and various **machine learning models** for the back-end. The app predicts whether a person is at risk of heart disease based on the medical data provided.

### Features:
- Predicts the likelihood of heart disease using different machine learning models.
- Easy-to-use web interface built with Streamlit.
- Displays prediction results in an understandable format.
- Visualizes key insights from the dataset.

## Technologies Used

- **Streamlit**: For building the web application.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Scikit-learn**: For machine learning models and metrics.
- **Matplotlib** & **Seaborn**: For visualizing data.
- **Pickle**: For saving and loading trained models.

## Installation

To run this project locally, you need to set up a Python environment and install the dependencies.

### Requirements:

- Python 3.7+
- pip (Python package installer)

### Steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Rajaefr/heartDesease.git
   cd heartDesease
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Once all dependencies are installed, you can run the application with the following command:

```bash
streamlit run app.py
```

This will open the application in your default web browser where you can interact with it and predict heart disease risk.

Or access the **deployed app** directly here:  
👉 [https://heartdeseas-rj.streamlit.app/](https://heartdeseas-rj.streamlit.app/)

## Models Used

The app includes several machine learning models for heart disease classification:

1. **Logistic Regression**
2. **Decision Tree Classifier**
3. **Random Forest Classifier**
4. **Support Vector Machine (SVM)**
5. **K-Nearest Neighbors (KNN)**
6. **Naive Bayes Classifier**

You can choose the model to use for prediction through the app interface.

## How to Run Locally

To run the app locally, follow the installation steps mentioned above. Once the setup is complete, run the following command:

```bash
streamlit run app.py
```

After running the above command, the app will open in your default web browser at `localhost:8501`.

## File Structure

```
heartDesease/
│
├── app.py                  # Main Streamlit application file
├── model.pkl               # Trained machine learning model
├── scaler.pkl              # StandardScaler object for preprocessing
├── heart.csv               # Dataset used for training the model (if necessary)
├── requirements.txt        # List of dependencies
└── README.md               # This file
```

## Collaborators

This project was developed in collaboration with:

- **Zainab Abdenour** – [GitHub Profile](https://github.com/zainab-gutten)

## License

This project is licensed under the MIT License .
