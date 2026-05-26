import requests

url = "http://www.practicepython.org/assets/nameslist.txt"
response = requests.get(url)
content = response.text

#Sauvegarde de les valeur
with open("nameslist.txt", "w", encoding = "utf-8") as f:
    f.write(content)

# oprérations
with open("nameslist.txt", "r", encoding="utf-8") as f:
    #Read the file line by line
    for line in f:
        print(line.strip())
    
    f.seek(0)

    # read only the 5th line of the line
    lines = f.readlines()
    if len(lines) >= 5:
        print(f"5ème ligne: {lines[4].strip()}")
    
    f.seek(0)

    #Read only the 5 first characters of the file
    print(f.read(5))

# --- MANIPULATION DES DONNÉES ---

with open("nameslist.txt", "r", encoding="utf-8") as f:
    names_list = [line.strip() for line in f.readlines()]
    letters_list = [list(name) for name in names_list]
    print(letters_list)

# Compter les occurrences de "Darth", "Luke" et "Lea"
counts = {
    "Darth": names_list.count("Darth"),
    "Luke": names_list.count("Luke"),
    "Lea": names_list.count("Lea"),
}
print(f"\nOccurrences : {counts}")

# --- ÉCRITURE ET MODIFICATION ---

# Ajouter ton prénom à la fin du fichier
with open("nameslist.txt", "a", encoding="utf-8") as f:
    f.write("\nYadjiman")

# Ajouter "SkyWalker" à côté de chaque "Luke"
# Pour cela, on doit réécrire le fichier
with open("nameslist.txt", "r", encoding="utf-8") as f:
    content_lines = f.readlines()

    new_list = []
    for line in content_lines:
        if line.strip() == "Luck":
            new_list.append("Luke SkyWalker\n")
        else:
            new_list.append(line)

with open("nameslist.txt", "w", encoding="utf-8") as f:
    f.writelines(new_list)

print("\nFichier mis à jour avec succès!")
