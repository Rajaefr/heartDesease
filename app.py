import streamlit as st
import numpy as np
import pickle
import os
import base64

# ✅ La toute première commande doit être set_page_config
st.set_page_config(page_title="HeartCare", page_icon="❤️", layout="centered")

# Charger les styles CSS
def apply_css():
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            font-family: 'Arial', sans-serif;
        }
        .stAppHeader {
            background: #df1010;
            border: 1px solid white;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            color: white;
            margin-bottom: 20px;
        }
        .stAppHeader h1 {
            text-align: center;
        }
        h1 {
            font-size: 32px;
            white-space: nowrap;
            text-align: center;
        }
        .text-content p {
            color: white;
        }
        .text-container {
            background: rgba(223, 16, 16, 0.7);
            width: 600px;
            padding: 22px;
            border-radius: 8px;
            box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px;
            display: flex;
            align-items: center;
            border: 1px solid white;
            justify-content: space-between;
        }
        .stApp {
            background-image: linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%);
        }
        .gif-container {
            flex-shrink: 0;
            margin-top: 25px;
            margin-left: 15px;
            display: flex;
            align-items: left;
            justify-content: center;
            background: transparent;
            border: #df1010 2px solid;
            border-radius: 12px;
            box-shadow: rgba(0, 0, 0, 0.19) 0px 10px 20px, rgba(0, 0, 0, 0.23) 0px 6px 6px;
        }
        .gif-container img {
            width: 300px;
            height: auto;
            transition: transform 0.3s ease-in-out;
        }
        .gif-container img:hover {
            transform: scale(1.1);
        }
        .stButton > button {
            display: block;
            margin: 50px auto;
            background: #df1010;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
            border: 1px solid #df1010;
            transition: all 0.3s ease-in-out;
            width: 200px;
        }
        .stButton > button:hover {
            background: linear-gradient(95deg, #df1010, #f5f1f1);
            transform: scale(1.05);
            color: white;
        }
        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            backdrop-filter: blur(5px);
            z-index: 999;
        }
        .popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            padding: 2rem;
            border-radius: 5px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.2);
            z-index: 1001;
            width: 90%;
            max-width: 500px;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Charger le modèle et le scaler
@st.cache_resource
def load_model_and_scaler():
    try:
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
        with open("scaler.pkl", "rb") as f:
            scaler = pickle.load(f)
        return model, scaler
    except FileNotFoundError:
        st.error("Erreur critique : Fichiers de modèle manquants!")
        return None, None

# Page d'accueil
def accueil():
    apply_css()
    col1, col2 = st.columns([3, 2], gap="large")
    with col1:
        st.markdown(
            """
            <div class="text-container">
                <div class="text-content">
                    <h1 style="color:white;">Bienvenue sur HeartCare</h1>
                    <p class="lead">HeartCare vous aide à évaluer votre risque cardiaque en quelques clics. Lancez votre diagnostic dès maintenant !</p>
                </div>
                <div class="gif-container">
                    <img src="https://tinyurl.com/34x9u89m" width="150">
                </div>
            </div>
            """,
            unsafe_allow_html=True )
    if st.button("Commencer", key="start-btn"):
        st.session_state.page = "diagnostic"
        st.session_state.form_step = 1
        st.rerun()

# Page Diagnostic
def diagnostic():
    apply_css()

    if "form_step" not in st.session_state:
        st.session_state.form_step = 1

    current_step = st.session_state.form_step

    model, scaler = load_model_and_scaler()
    if not model or not scaler:
        return

    total_steps = 3

    with st.form("cardio_form"):
        st.markdown(f'<div class="form-step" style="color:#df1010; font-weight:bold;">Étape {current_step}/{total_steps}</div>', unsafe_allow_html=True)
        st.progress(current_step / total_steps)

        cols = st.columns(2)
        user_inputs = {}

        if current_step == 1:
            with cols[0]:
                user_inputs['age'] = st.number_input("Âge", min_value=10, max_value=120, step=1)
                user_inputs['sex'] = 1 if st.selectbox("Sexe", ["Homme", "Femme"]) == "Homme" else 0
                cp_mapping = {
                    "Angine typique": 0,
                    "Angine atypique": 1,
                    "Douleur non-angineuse": 2,
                    "Asymptomatique": 3
                }
                user_inputs['cp'] = cp_mapping[st.selectbox("Type de douleur thoracique", list(cp_mapping.keys()))]

            with cols[1]:
                user_inputs['trestbps'] = st.number_input("Pression artérielle au repos (mmHg)", min_value=50, max_value=200, step=1)
                restecg_mapping = {
                    "Normal": 0,
                    "Anomalie onde ST-T": 1,
                    "Hypertrophie ventriculaire gauche": 2
                }
                user_inputs['restecg'] = restecg_mapping[st.selectbox("ECG au repos", list(restecg_mapping.keys()))]

        elif current_step == 2:
            with cols[0]:
                user_inputs['chol'] = st.number_input("Cholestérol (mg/dl)", min_value=100, max_value=600, step=1)
                user_inputs['fbs'] = 1 if st.selectbox("Glycémie à jeun > 120mg/dl", ["Non", "Oui"]) == "Oui" else 0
            with cols[1]:
                user_inputs['thalach'] = st.number_input("Fréquence cardiaque max", min_value=50, max_value=250, step=1)
                user_inputs['exang'] = 1 if st.selectbox("Angine à l'effort", ["Non", "Oui"]) == "Oui" else 0

        elif current_step == 3:
            with cols[0]:
                user_inputs['oldpeak'] = st.number_input("Dépression ST", min_value=0.0, max_value=10.0, step=0.1)
                slope_mapping = {
                    "Plate": 0,
                    "Descendante": 1,
                    "Montante": 2
                }
                user_inputs['slope'] = slope_mapping[st.selectbox("Pente ST", list(slope_mapping.keys()))]
            with cols[1]:
                user_inputs['ca'] = st.selectbox("Vaisseaux colorés", [0, 1, 2, 3])
                thal_mapping = {
                    "Normal": 1,
                    "Défaut fixe": 2,
                    "Défaut réversible": 3
                }
                user_inputs['thal'] = thal_mapping[st.selectbox("Thalassémie", list(thal_mapping.keys()))]

        # Navigation
        col1_nav, col2_nav, col3_nav = st.columns([1, 2, 1])
        with col1_nav:
            if st.form_submit_button("Retour à l'accueil"):
                st.session_state.page = "accueil"
                st.session_state.form_step = 1
                st.rerun()
        with col3_nav:
            if current_step < total_steps:
                if st.form_submit_button("Suivant", type="primary"):
                    st.session_state.form_step += 1
                    st.rerun()
            else:
                if st.form_submit_button("🔍 Résultats", type="primary"):
                    st.session_state.result = np.random.choice([0, 1])
                    st.session_state.show_popup = True
                    st.rerun()

    # Résultat
    if st.session_state.get("show_popup", False):
        result = st.session_state.result
        st.markdown(
            """
            <div class="overlay"></div>
            <div class="popup" style="color:white;background: #df1010;">
                <h2>{title}</h2>
                <p>{message}</p>
            </div>
            """.format(
                title="Risque cardiaque détecté!" if result else "Aucun risque détecté",
                message="Consultez un spécialiste rapidement!" if result else "Continuez à prendre soin de votre cœur!"
            ),
            unsafe_allow_html=True
        )

def main():
    if "page" not in st.session_state:
        st.session_state.page = "accueil"
    if st.session_state.page == "accueil":
        accueil()
    elif st.session_state.page == "diagnostic":
        diagnostic()

if __name__ == "__main__":
    main()
