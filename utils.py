import streamlit as st

def load_css(css_file_path: str):
    """
    Charge un fichier CSS local en UTF-8 et l'injecte dans l'application Streamlit.
    """
    try:
        with open(css_file_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"⚠️ Fichier CSS introuvable : {css_file_path}")
    except UnicodeDecodeError:
        st.error("❌ Erreur d'encodage : vérifiez que le fichier CSS est bien enregistré en UTF-8.")
