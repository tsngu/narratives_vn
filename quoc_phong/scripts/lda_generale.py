import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora, models
import pyLDAvis.gensim_models
import gensim


# Charger la liste de stopwords depuis un fichier .txt
with open("../txt/stopwords_vn.txt", "r", encoding="utf-8") as f:
    custom_stopwords = set(f.read().splitlines())

# Fonction de prétraitement du texte
def preprocess_text(text):
    tokens = word_tokenize(text)  # Tokenisation
    tokens = [token.lower() for token in tokens if token.isalpha()]  # Supprimer la ponctuation et mise en minuscules
    tokens = [token for token in tokens if token not in custom_stopwords]  # Supprimer les stopwords personnalisés
    return tokens

# Fonction pour lire un fichier texte
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Traitement des trois dossiers
folder_paths = ["../output/vnp/", "../output/btt/", "../output/nd/"]
all_documents = []

for folder_path in folder_paths:
    print(f"Traitement du dossier {folder_path}...")
    documents = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith(".txt"):
            print(f"Lecture du fichier {file_name}...")
            document = read_text_file(file_path)
            preprocessed_doc = preprocess_text(document)
            documents.append(preprocessed_doc)
    all_documents.append(documents)

# Créer un dictionnaire et une matrice de documents
dictionary = corpora.Dictionary(sum(all_documents, []))
corpus = [dictionary.doc2bow(doc) for doc in sum(all_documents, [])]

# Entraîner le modèle LDA
lda_model = models.LdaModel(corpus, num_topics=10, id2word=dictionary, passes=15)

# Visualisation des résultats
vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)

# Sauvegarder la visualisation dans un fichier HTML
pyLDAvis.save_html(vis, '../output/lda_generale.html')