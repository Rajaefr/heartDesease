# 🩺 Prédiction des Maladies Cardiaques  

Ce projet utilise le **Machine Learning** pour prédire le risque de maladies cardiaques à partir d'un ensemble de données médicales. Plusieurs modèles d’apprentissage automatique sont testés pour identifier le plus performant. Une interface interactive est également disponible via **Streamlit**.

## 🚀 Fonctionnalités  

- 📊 **Analyse des données** : Visualisation et exploration du dataset  
- 🔍 **Modèles de Machine Learning** :  
  - Régression Logistique  
  - Arbre de Décision  
  - Random Forest  
  - SVM  
  - Réseau de Neurones  
- 🏆 **Sélection du meilleur modèle** en fonction des performances  
- 🌐 **Interface Web interactive** avec Streamlit  

## 📂 Structure du projet  

```
📂 heart-disease-prediction  
│── 📜 heart.csv               # Dataset utilisé  
│── 📜 model.pkl               # Modèle ML sauvegardé  
│── 📜 scaler.pkl              # StandardScaler sauvegardé  
│── 📜 app.py                  # Application Streamlit  
│── 📜 train.py                # Script d'entraînement du modèle  
│── 📜 README.md               # Documentation  
```

## 📊 Installation et Exécution  

1️⃣ **Cloner le dépôt**  
```bash
git clone https://github.com/ton-utilisateur/heart-disease-prediction.git
cd heart-disease-prediction
```

2️⃣ **Installer les dépendances**  
```bash
pip install -r requirements.txt
```

3️⃣ **Lancer l'entraînement du modèle**  
```bash
python train.py
```

4️⃣ **Démarrer l'application Streamlit**  
```bash
streamlit run app.py
```

## 📌 Exemples de Prédiction  

Un exemple de prédiction avec un nouvel ensemble de données :  
```python
import pickle
import numpy as np

# Charger le modèle et le scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Nouvelle donnée (âge, sexe, douleur thoracique, etc.)
new_data = np.array([[63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]])
new_data_scaled = scaler.transform(new_data)
prediction = model.predict(new_data_scaled)[0]

print(f"Prédiction : {'Maladie cardiaque' if prediction == 1 else 'Pas de maladie cardiaque'}")
```

## 🔗 Ressources  
- Dataset : [Heart Disease UCI](https://www.kaggle.com/datasets/ronitf/heart-disease-uci)  
- Documentation Sklearn : [scikit-learn](https://scikit-learn.org/)  
- Streamlit : [Documentation](https://docs.streamlit.io/)  

---
