from googletrans import Translator

def creer_dictionnaire_traduction():
    # 1. Notre liste de départ
    french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
    
    # 2. Initialisation du traducteur Google
    # On crée une instance de la classe Translator
    translator = Translator()
    
    # 3. Création d'un dictionnaire vide pour stocker les résultats
    translation_dict = {}
    
    print("Traduction en cours...")
    
    # 4. Boucle sur chaque mot de la liste française
    for word in french_words:
        try:
            # On demande la traduction vers l'anglais (dest='en')
            # .text permet d'extraire uniquement la chaîne de caractères traduite
            translation = translator.translate(word, src='fr', dest='en').text
            
            # On ajoute le couple {Français: Anglais} au dictionnaire
            translation_dict[word] = translation
            
        except Exception as e:
            print(f"Erreur lors de la traduction de '{word}': {e}")

    # 5. Affichage du résultat final
    return translation_dict

# Exécution du script
if __name__ == "__main__":
    resultat = creer_dictionnaire_traduction()
    print("\n--- Résultat final ---")
    print(resultat)