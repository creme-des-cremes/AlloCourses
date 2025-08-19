import streamlit as st
from frontend.passer_commande import passer_commande
from frontend.zones_tarifs import zones_tarifs
from frontend.contact import contact
from frontend.temoignages import temoignages
from utils import load_css

# ✅ Configuration initiale de la page
st.set_page_config(
    page_title="AlloCourses - Livraisons à domicile à Dakar",
    page_icon="🛒",
    layout="centered"
)

# ✅ Chargement du style CSS
load_css("styles/style.css")

# ✅ Page active par défaut
if "page" not in st.session_state:
    st.session_state.page = "accueil"

# ✅ Barre de navigation
st.markdown("""
<div style='display: flex; justify-content: center; gap: 30px; background-color: #f9f9f9; padding: 10px 0; border-bottom: 1px solid #ddd;'>
    <a href='?page=accueil' style='text-decoration: none; color: #0b3c61; font-weight: bold;'>🏠 Accueil</a>
    <a href='?page=commande' style='text-decoration: none; color: #0b3c61;'>📋 Commander</a>
    <a href='?page=zones' style='text-decoration: none; color: #0b3c61;'>📍 Tarifs</a>
    <a href='?page=contact' style='text-decoration: none; color: #0b3c61;'>📞 Contact</a>
    <a href='?page=temoignages' style='text-decoration: none; color: #0b3c61;'>💬 Témoignages</a>
</div>
""", unsafe_allow_html=True)

# ✅ Gestion des pages
params = st.query_params
if "page" in params:
    st.session_state.page = params["page"]

if st.session_state.page == "accueil":
    col1, col2, col3 = st.columns([2, 2, 1])
    with col2:
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        st.image("logo.jpeg", width=100)

    st.markdown("""
    <h1 style='text-align: center;'>📞Bienvenue chez <span style='color:#FFF3C4;'>AlloCourses</span> 🛒</h1>
    <p style='text-align: center; font-size:18px;'>Le moyen le plus simple et rapide de faire vos courses à Dakar</p>
    """, unsafe_allow_html=True)

    st.markdown("""
    ---
    ### 🚀 Pourquoi choisir AlloCourses ?
     Fatigué(e) des files d'attente et des allées de supermarché ? AlloCourses vous simplifie la vie. On fait vos courses pour vous avec dynamisme et efficacité, et on vous les livre chez vous. L'idéal pour tous ceux qui manquent de temps ou d'énergie. Laissez-nous faire, vous avez mieux à faire 🩵😉

    Parce qu’on a tous des journées où le temps manque… et c’est là qu’**AlloCourses** devient votre meilleur allié.

    - 🎉 **Un baptême, un mariage, une cérémonie à organiser ?** Pas de panique ! On gère vos courses pendant que vous vous concentrez sur l'essentiel.
    - 🧳 **Vous venez d’arriver à Dakar ?** En déplacement ou en court séjour ? Évitez les files et les détours, on achète et on vous livre ce qu’il vous faut, où il vous faut.
    - 🎁 **Besoin d’un cadeau de dernière minute ?** Une surprise à offrir ou un geste urgent à faire ? Dites-nous quoi, et on le fait pour vous.
    - 🕒 **Vous êtes débordé(e) ?** Au travail, enfants à gérer, transports imprévus ou simplement fatigué  ? Notre équipe s’occupe de tout, même à la dernière minute !

    ---
    ### 👨‍👩‍👧‍👦 Ce que nous offrons :

    - **🛍️ Simplicité** : Commande rapide par téléphone ou en ligne
    - **🚚 Réactivité** : Livraison express dans tout Dakar
    - **💳 Sécurité** : Paiement fiable (Orange Money, Wave, espèces)
    - **⏱️ Gain de temps** : Plus besoin de vous déplacer

    ---
    ### 💡 Qui sommes-nous ?

    AlloCourses est un service 100% dakarois pensé pour vous simplifier la vie.  
    Notre équipe fiable, rapide et discrète effectue vos courses avec soin, selon vos préférences, puis vous les livre où que vous soyez.

    > **Confort, rapidité, fiabilité** : AlloCourses, c’est votre réflexe malin pour faire vos achats à Dakar.
    """)

elif st.session_state.page == "commande":
    passer_commande()
elif st.session_state.page == "zones":
    zones_tarifs()
elif st.session_state.page == "contact":
    contact()
elif st.session_state.page == "temoignages":
    temoignages()
else:
    st.error("❌ Page introuvable. Revenez à l'accueil.")

# ✅ Pied de page
st.markdown("""
<style>
.footer {
    background-color:#f9f9f9;
    padding: 20px 10px;
    margin-top: 40px;
    border-top: 1px solid #ccc;
    text-align: center;
    font-size: 14px;
    color: #0b3c61;
}
.footer a {
    color: #E50914;
    text-decoration: none;
    font-weight: bold;
}
.footer a:hover {
    text-decoration: underline;
}
</style>

<div class='footer'>
    📍 Dakar, Sénégal | 📞 <strong>+221 71 050 84 66</strong><br>
    Suivez-nous sur 
    <a href='https://www.facebook.com/share/1a4UwtXRdf/' target='_blank'>Facebook</a> <br>
    &copy; 2025 <strong>AlloCourses</strong>. Tous droits réservés.
</div>
""", unsafe_allow_html=True)
