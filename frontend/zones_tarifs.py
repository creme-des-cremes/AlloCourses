import streamlit as st

def zones_tarifs():
    st.markdown("<h2 style='text-align: center;'>📍 Zones desservies & Tarification</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Voici une estimation des frais selon votre localisation, le temps de courses et le poids des articles.</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🚚 Zones de livraison depuis notre agence (Nord Foire)")

    st.markdown("""
    Nous livrons partout à **Dakar**, depuis notre point de départ à **Nord Foire**.

    👉 Les tarifs ci-dessous sont **des estimations générales**.  
    Pour obtenir un **calcul exact et personnalisé**, veuillez **télécharger l'application AlloCourses sur le Play Store**.
    """)

    st.markdown("""
    ---
    ### 💰 Estimation globale par zone

    | Zone               | Distance approximative | Frais de transport (Aller/Retour) | Temps moyen au supermarché | Poids moyen estimé | Coût AlloCourses estimé |
    |--------------------|------------------------|---------------------------|-----------------------------|---------------------|--------------------------|
    | Proche (≤ 5 km)    | Yoff, Ouakam, Almadies | 3 000 FCFA                | 1HOO min                    | 10 kg              | 6 000 FCFA               |
    | Moyenne (6-10 km)  | Liberté 6, Mermoz, HLM | 5 000 FCFA                | 2H00 min                    | 15 kg              | 12 000 FCFA               |
    | Éloignée (> 10 km) | Plateau, Parcelles...  | 6 000 FCFA                | 3H00  min                   | 20 kg              | 18 000 FCFA               |
    """)

    st.info("📦 Le tarif du **transport** dépend du trajet complet **Nord Foire → Supermarché → Client**. NB:le PAYEMENT du service de livraison est independant du service Allocourses")

    st.markdown("---")
    st.subheader("📊 Catalogue indicatif (prix moyen/kg)")

    st.markdown("""
    | Article                | Prix moyen (FCFA/kg) | Exemple poids | Coût estimé |
    |------------------------|----------------------|----------------|-------------|
    | Riz parfumé            | 800 FCFA             | 5 kg           | 4 000 FCFA  |
    | Tomates fraîches       | 600 FCFA             | 2 kg           | 1 200 FCFA  |
    | Pommes de terre        | 500 FCFA             | 3 kg           | 1 500 FCFA  |
    | Sucre en poudre        | 750 FCFA             | 2 kg           | 1 500 FCFA  |
    | Viande de bœuf         | 3 000 FCFA           | 1 kg           | 3 000 FCFA  |
    | Poisson frais (Thiof)  | 3 500 FCFA           | 1 kg           | 3 500 FCFA  |
    | Oignons                | 400 FCFA             | 2 kg           | 800 FCFA    |
    | Bananes                | 700 FCFA             | 1 kg           | 700 FCFA    |
    """)

    st.markdown("""
    📝 Ces prix sont fournis à titre **indicatif**, selon les supermarchés partenaires et les saisons.

    ---
    📱 Pour une estimation personnalisée et dynamique, téléchargez l’application **AlloCourses** sur le **Play Store**.  
    📞 Pour toute question spéciale : **+221 XX XXX XX XX**
    """)
