import os
import csv
import sys

def lire_fichier_csv(fichier):
    phrases = []
    with open(fichier, 'r', encoding='utf-8') as f:
        lecteur_csv = csv.reader(f, delimiter='\t')
        phrase_actuelle = []
        for ligne in lecteur_csv:
            if ligne:  # Vérifie si la ligne n'est pas vide
                phrase_actuelle.append(ligne)
            else:
                phrases.append(phrase_actuelle)
                phrase_actuelle = []
        if phrase_actuelle:
            phrases.append(phrase_actuelle)
    return phrases

def extraire_associations_sub_root_cau(phrases):
    associations_sub_root_cau = []
    for phrase in phrases:
        sujet = None
        verbe = None
        cause = None
        for mot in phrase:
            if mot[-1] == 'sub':
                sujet = mot[1]
            elif mot[-1] == 'root':
                verbe = mot[1]
            elif mot[-1] == 'prp':
                cause = mot[1]
        if sujet and verbe and cause:
            associations_sub_root_cau.append((sujet, verbe, cause))
    return associations_sub_root_cau

# Vérification des arguments en ligne de commande
if len(sys.argv) != 2:
    print("Utilisation: python script.py dossier_entree")
    sys.exit(1)

dossier_entree = sys.argv[1]

# Vérification si le dossier d'entrée existe
if not os.path.isdir(dossier_entree):
    print("Le dossier d'entrée spécifié n'existe pas.")
    sys.exit(1)

# Générer le nom du fichier de sortie
nom_fichier_sortie = "resultats_sub_root_cau.csv"

# Ouvrir le fichier de sortie en mode écriture
with open(nom_fichier_sortie, 'w', newline='', encoding='utf-8') as f_out:
    csv_writer = csv.writer(f_out)
    
    # Écrire les noms de colonnes dans le fichier CSV
    csv_writer.writerow(['Sujet', 'Verbe', 'PRP'])
    
    # Parcourir les fichiers dans le dossier d'entrée
    for fichier in os.listdir(dossier_entree):
        if fichier.endswith('.csv'):
            chemin_fichier_entree = os.path.join(dossier_entree, fichier)
            phrases = lire_fichier_csv(chemin_fichier_entree)
            associations_sub_root_cau = extraire_associations_sub_root_cau(phrases)
            for association in associations_sub_root_cau:
                csv_writer.writerow(association)

