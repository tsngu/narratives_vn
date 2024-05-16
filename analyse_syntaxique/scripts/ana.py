import os
import csv

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

def extraire_sujet_verbe_cod(phrases):
    sujet_verbe_cod = []
    for phrase in phrases:
        sujet = None
        verbe = None
        cod = None
        for mot in phrase:
            if mot[-1] == 'sub':
                sujet = mot[1]
            elif mot[-1] == 'dob':
                cod = mot[1]
            elif mot[-1] == 'root':  # Le rôle 'root' est généralement le verbe principal de la phrase
                verbe = mot[1]
        if sujet and verbe and cod:
            sujet_verbe_cod.append((sujet, verbe, cod))
    return sujet_verbe_cod


# Chemin vers le dossier contenant les fichiers
dossier_entree = "./nd"
fichier_sortie = "./resultats_suj_cod.csv"

with open(fichier_sortie, 'w', newline='', encoding='utf-8') as f_out:
    csv_writer = csv.writer(f_out)
    for fichier in os.listdir(dossier_entree):
        if fichier.endswith('.csv'):
            chemin_fichier_entree = os.path.join(dossier_entree, fichier)
            phrases = lire_fichier_csv(chemin_fichier_entree)
            sujet_verbe_cod = extraire_sujet_verbe_cod(phrases)
            for sujet, verbe, cod in sujet_verbe_cod:
                csv_writer.writerow([fichier, sujet, verbe, cod])
