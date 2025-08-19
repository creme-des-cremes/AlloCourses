import streamlit as st
from utils import load_css

def passer_commande():
    load_css("styles/style.css")

    st.markdown("""
    <h2 style='text-align: center;'>🛒 Passer une commande</h2>
    <p style='text-align: center;'>Cliquez sur le bouton ci-dessous pour accéder au formulaire de commande.</p>
    """, unsafe_allow_html=True)

    # Nouveau bouton vers page externe
    st.markdown("""
    <a href="https://creme-des-cremes.github.io/AlloCoursesFormulaires/commande.html" target="_blank">
      <button style="padding:12px 24px; background-color:#0b3c61; color:white; border:none; border-radius:5px; font-size:16px;">
        📝 Passer une commande
      </button>
    </a>
    """, unsafe_allow_html=True)

    st.markdown("""
    ---
    📞 Besoin d'aide ? Contactez-nous au **+221 71 050 84 66**  
    📍 Livraison uniquement à Dakar pour le moment.
    """, unsafe_allow_html=True)
