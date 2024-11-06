import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import messagebox

# Initialisation du moteur de synthèse vocale
engine = pyttsx3.init()


# Fonction pour lire à voix haute un message
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Fonction pour la reconnaissance vocale (microphone -> texte)
def listen():
    recognizer = sr.Recognizer()

    # Utiliser le microphone comme source d'entrée
    with sr.Microphone() as source:
        print("Veuillez parler...")
        recognizer.adjust_for_ambient_noise(source)  # Ajuste l'environnement pour les bruits de fond
        audio = recognizer.listen(source)

    try:
        # Utiliser Google Speech Recognition pour convertir l'audio en texte
        print("Vous avez dit : " + recognizer.recognize_google(audio, language='fr-FR'))
        return recognizer.recognize_google(audio, language='fr-FR')
    except sr.UnknownValueError:
        print("Google Speech Recognition n'a pas compris l'audio")
        return None
    except sr.RequestError as e:
        print("Impossible d'obtenir des résultats de Google Speech Recognition; {0}".format(e))
        return None


# Fonction pour mettre à jour l'interface graphique avec le texte reconnu
def update_text(text):
    text_display.config(state=tk.NORMAL)
    text_display.delete(1.0, tk.END)  # Effacer l'ancien texte
    text_display.insert(tk.END, text)  # Insérer le nouveau texte
    text_display.config(state=tk.DISABLED)


# Fonction principale de l'application
def main():
    speak("Bienvenue dans l'application de reconnaissance et de synthèse vocale.")

    while True:
        print("Dites 'stop' pour quitter.")
        text = listen()

        if text is None:
            continue

        # Mise à jour de l'interface graphique avec le texte reconnu
        update_text(text)

        # Si l'utilisateur dit "stop", arrêter le programme
        if 'stop' in text.lower():
            speak("Arrêt de l'application.")
            print("Arrêt de l'application.")
            break

        # Sinon, lire le texte
        speak("Vous avez dit: " + text)


# Fonction pour démarrer l'application en mode GUI
def start_gui():
    global text_display

    # Créer la fenêtre principale de l'application
    root = tk.Tk()
    root.title("Application de reconnaissance vocale")

    # Créer une zone de texte pour afficher le texte reconnu
    text_display = tk.Text(root, height=10, width=50, wrap=tk.WORD, font=("Helvetica", 14))
    text_display.pack(padx=10, pady=10)

    # Créer un bouton pour démarrer l'écoute
    start_button = tk.Button(root, text="Démarrer l'écoute", command=lambda: main())
    start_button.pack(padx=10, pady=10)

    # Afficher une alerte de bienvenue
    messagebox.showinfo("Bienvenue", "Bienvenue dans l'application de reconnaissance vocale!")

    # Lancer l'interface graphique
    root.mainloop()


# Exécution de l'application
if __name__ == "__main__":
    start_gui()
