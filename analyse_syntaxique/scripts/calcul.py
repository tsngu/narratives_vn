import csv
from collections import defaultdict


fichier = 'resultats_suj_cod.csv' 

def colonne(file, n, sep=',') : 
    with open(file, "r") as f: 
        r = csv.reader(f, delimiter = sep)
        rlignes = list(zip(*r))
        if (n <len(rlignes)) and (n>= -len(rlignes)):  
            return rlignes [n]
        else : 
            return[]
        

def wordListToFreqDict(liste_mots):
    freqs_mots = [liste_mots.count(mot) for mot in liste_mots]
    return dict(list(zip(liste_mots,freqs_mots)))
    
def sortFreqDict(freqs_mots):
    aux = [(freqs_mots[mot], mot) for mot in freqs_mots]
    aux.sort()
    aux.reverse()
    return aux

if __name__ == "__main__": 
    c = colonne(fichier, 1, sep=",")
    print(type(c)) 
    res = wordListToFreqDict(c)
    print(res)
    frequences_ordre = 

            
    

