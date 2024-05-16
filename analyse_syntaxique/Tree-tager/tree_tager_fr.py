import os
import csv
import treetaggerwrapper

# Chemin vers le dossier contenant les fichiers texte en français
dossier_texte = "./nv_corpus/vnp_fr"

# Chemin vers le dossier où seront sauvegardés les fichiers CSV
dossier_resultat = "./output/vnp_fr_output"

# Configuration de TreeTagger
chemin_treetagger = "../tree-tagger-linux-3.2.5"
modele_treetagger = "../tree-tagger-linux-3.2.5/lib/french.par"
tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr', TAGDIR=chemin_treetagger, TAGPARFILE=modele_treetagger)

def annoter_morphosyntaxe_fichier(fichier_texte):
    with open(fichier_texte, "r", encoding="utf-8") as f:
        texte = f.read()
        tags = tagger.tag_text(texte)
        annotations = [tag.split("\t") for tag in tags]
        return annotations

def sauvegarder_annotations_csv(annotations, fichier_csv):
    with open(fichier_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(annotations)

def annoter_dossier(dossier_texte, dossier_resultat):
    if not os.path.exists(dossier_resultat):
        os.makedirs(dossier_resultat)
    
    for fichier in os.listdir(dossier_texte):
        if fichier.endswith(".txt"):
            fichier_texte = os.path.join(dossier_texte, fichier)
            annotations = annoter_morphosyntaxe_fichier(fichier_texte)
            fichier_csv = os.path.join(dossier_resultat, f"{os.path.splitext(fichier)[0]}.csv")
            sauvegarder_annotations_csv(annotations, fichier_csv)

if __name__ == "__main__":
    annoter_dossier(dossier_texte, dossier_resultat)
    print("Annotations morphosyntaxiques terminées.")

