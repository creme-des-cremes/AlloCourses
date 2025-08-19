import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

def envoyer_email_commande(nom, telephone, adresse, nb_articles, liste_articles, commentaire, date_livraison):
    expediteur = "allahyallydie@gmail.com"
    destinataire = "allahyallydie@gmail.com"
    mot_de_passe_app = os.getenv("EMAIL_PASSWORD")  # Chargé depuis .env ✅

    sujet = "📦 Nouvelle commande sur AlloCourses"
    corps = f"""
    👤 Nom : {nom}
    📞 Téléphone : {telephone}
    📍 Adresse : {adresse}
    🧺 Nombre d’articles : {nb_articles}
    📝 Liste : {liste_articles}
    💬 Commentaire : {commentaire}
    📅 Date de livraison : {date_livraison}
    """

    message = MIMEMultipart()
    message["From"] = expediteur
    message["To"] = destinataire
    message["Subject"] = sujet
    message.attach(MIMEText(corps, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as serveur:
            serveur.login(expediteur, mot_de_passe_app)
            serveur.sendmail(expediteur, destinataire, message.as_string())
        return True
    except Exception as e:
        print("Erreur lors de l'envoi :", e)
        return False
