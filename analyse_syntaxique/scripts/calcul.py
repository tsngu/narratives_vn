import csv

def colonne(file, n, sep=','):
    with open(file, "r") as f:
        r = csv.reader(f, delimiter=sep)
        rlignes = list(zip(*r))
        if (-len(rlignes) <= n < len(rlignes)):
            return rlignes[n]
        else:
            return []

def wordListToFreqDict(liste_mots):
    freqs_mots = {mot: liste_mots.count(mot) for mot in liste_mots}
    return freqs_mots

def sortFreqDict(freqs_mots):
    return sorted(freqs_mots.items(), key=lambda x: x[1], reverse=True)[:100]

if __name__ == "__main__":
    fichier = 'resultats_suj_cod.csv'
    c = colonne(fichier, 1)
    print("Type de la colonne :", type(c))
    res = wordListToFreqDict(c)
    print("Dictionnaire de fréquence des mots :", res)
    frequences_ordre = sortFreqDict(res)
    print("Les 100 premières fréquences des mots ordonnées :", frequences_ordre)