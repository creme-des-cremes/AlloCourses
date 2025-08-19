import streamlit as st
from utils import load_css

def contact():
    # Chargement du style CSS global
    load_css("styles/style.css")

    # Titre principal
    st.markdown("""
    <h2 style='text-align: center;'>📞 Contact & Assistance</h2>
    <p style='text-align: center;'>Une question, un besoin particulier ou une commande spéciale ? Contactez-nous directement !</p>
    """, unsafe_allow_html=True)

    # Coordonnées
    st.markdown("""
    ---
    ### 📱 Nos coordonnées :

    - **Téléphone / WhatsApp :** +221 71 050 84 66  
    - **Email :** allocoursesn@gmail.com  
    - **Instagram :** [@allocourses.sn](https://instagram.com/allocourses.sn)  
    - **Facebook :** [facebook.com/allocourses](https://facebook.com/allocourses)

    ⏰ **Horaires de disponibilité :**
    - Lundi à Samedi : 8h00 à 20h00  
    - Dimanche : Fermé
    """, unsafe_allow_html=True)

    # Nouveau bouton vers le formulaire HTML externe
    st.markdown("""
    ---
    ### ✍️ Formulaire de contact rapide

    <a href="https://creme-des-cremes.github.io/AlloCoursesFormulaires/contact.html" target="_blank">
      <button style="padding:12px 24px; background-color:#0b3c61; color:white; border:none; border-radius:5px; font-size:16px;">
        📨 Remplir le formulaire de contact
      </button>
    </a>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    ---
    📍 Nous sommes basés à Dakar, Sénégal
    """, unsafe_allow_html=True)
