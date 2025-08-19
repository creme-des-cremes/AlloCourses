import streamlit as st
from utils import load_css
import base64
import os

def temoignages():
    # Chargement du style
    load_css("styles/style.css")

    # Titre de la page
    st.markdown("""
    <h2 style='text-align: center;'>💬 Témoignages de nos clients</h2>
    <p style='text-align: center;'>Ils nous ont fait confiance… voici ce qu’ils pensent de notre service !</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Liste des témoignages
    temoins = [
        {
            "nom": "Fatou D. (Liberté 6)",
            "texte": "Service rapide et fiable, j’ai reçu toutes mes courses en moins de 2 heures ! Bravo à toute l’équipe.",
            "image": "frontend/fatou.jpg"
        },
        {
            "nom": "Mamadou S. (Parcelles Assainies)",
            "texte": "Je n’ai jamais eu un service aussi pratique. Même les articles difficiles à trouver ont été livrés.",
            "image": "frontend/mamadou.jpg"
        },
        {
            "nom": "Aïcha N. (Ngor)",
            "texte": "Très bonne communication, livreur courtois et les prix sont justes. Je recommande à 100%.",
            "image": "frontend/aicha.jpg"
        },
        {
            "nom": "Cheikh B. (Fass)",
            "texte": "J’étais sceptique au début mais franchement, ils m’ont sauvé plusieurs fois. Super utile !",
            "image": "frontend/cheikh.jpg"
        },
    ]

    # Affichage des témoignages avec photo
    for temoin in temoins:
        if os.path.exists(temoin["image"]):
            with open(temoin["image"], "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode()
            image_html = f"<img src='data:image/jpeg;base64,{encoded}' width='80' height='80' style='border-radius: 50%; margin-right: 15px; object-fit: cover;'>"
        else:
            image_html = "<div style='width:80px; height:80px; border-radius:50%; background:#ccc; display:inline-block; margin-right:15px;'></div>"

        st.markdown(f"""
        <div style='background-color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; box-shadow: 0px 2px 10px rgba(0,0,0,0.05); display: flex; align-items: center;'>
            {image_html}
            <div>
                <p style='color:#0b3c61; font-weight: bold; margin-bottom: 5px;'>{temoin['nom']}</p>
                <p style='margin-top: 0;'>{temoin['texte']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Lien vers formulaire externe
    st.markdown("---")
    st.markdown("<p style='text-align: center;'>Vous aussi, vous avez testé AlloCourses ?</p>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center;'>
        <a href="https://creme-des-cremes.github.io/AlloCoursesFormulaires/contact.html" target="_blank">
            <button style="padding:12px 24px; background-color:#0b3c61; color:white; border:none; border-radius:5px; font-size:16px; cursor:pointer;">
                📩 Laisser un témoignage maintenant
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Bouton retour accueil
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🏠 Retour à l'accueil", use_container_width=True):
        st.session_state.page = "accueil"
