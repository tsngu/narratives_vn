import requests
from requests.exceptions import SSLError
from bs4 import BeautifulSoup as bs
from tokenizer_vn import tokenize_vn
import string
from gensim import corpora
from gensim.models import LdaModel
import pyLDAvis.gensim_models
from tqdm import tqdm

def get_urls(fichier):
    with open(fichier, 'r') as file:
        urls = [line.strip() for line in file]
    return urls

def process_url(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            html = response.content
            soup = bs(html, "lxml")
            contenu_article = soup.find_all("p")
            contenu_article = contenu_article[:-3]
            return contenu_article
        else:
            print(f"Erreur : {url} a un status code : {response.status_code}")
            return None
    except SSLError as e:
        print(f"Erreur SSL lors de la requête à {url}: {e}")
        return None
    except Exception as e:
        print(f"Une erreur inattendue s'est produite lors de la requête à {url}: {e}")
        return None

def tokenize_content(contenu_article):
    sans_tag = [paragraphe.get_text() for paragraphe in contenu_article]
    contenu_tokenize = [tokenize_vn(text) for text in sans_tag]
    tokenized_contenu = []

    contenu_article = contenu_article[:-4]
    for paragraphe in contenu_article:
        
        texte = paragraphe.get_text()
        tokens = tokenize_vn(texte)
        tokens = [token for token in tokens if token not in string.punctuation]
        tokens = [token for token in tokens if any(c.isalpha() for c in token)]
        tokens = [token for token in tokens if token.lower() not in custom_sw]
        tokenized_contenu.append(tokens)

    return tokenized_contenu, contenu_tokenize

def train_lda(tokenized_contenu):
    dico = corpora.Dictionary(tokenized_contenu)
    corpus = [dico.doc2bow(tokens) for tokens in tokenized_contenu]
    lda_model = LdaModel(corpus, num_topics=5, id2word=dico, alpha='auto', eta='auto')

    return lda_model, dico, corpus

def lda_visualization(lda_model, dico, corpus):
    lda_visu = pyLDAvis.gensim_models.prepare(lda_model, corpus, dico)
    return lda_visu

def save_tokenization(contenu_tokenize, line_number):
    contenu_tokenize = contenu_tokenize[:-4]
    with open(f'../output/btt/btt_url_{line_number}.txt', 'w', encoding='utf-8') as file:
        for content in contenu_tokenize:
            file.write(' '.join(content) + '\n')

if __name__ == "__main__":
    stop_words_file = "../txt/stopwords_vn.txt"
    with open(stop_words_file, "r", encoding="utf-8") as sw:
        custom_sw = [line.strip() for line in sw]

    #urls_file = "article_urls.txt"
    urls_file = "../txt/urls_btt.txt"
    urls = get_urls(urls_file)

    all_content_tokenize = []
    for line_number, url in enumerate(tqdm(urls, desc="Processing URLs", unit="URL"), start=1):
        contenu_article = process_url(url)
        if contenu_article is not None:
            tokenized_contenu, contenu_tokenize = tokenize_content(contenu_article)
            save_tokenization(contenu_tokenize, line_number)
            all_content_tokenize.extend(tokenized_contenu)

    # Train LDA model on all content
    lda_model, dico, corpus = train_lda(all_content_tokenize)

    # Save LDA visualization for all content
    lda_visu = lda_visualization(lda_model, dico, corpus)
    pyLDAvis.save_html(lda_visu, '../output/btt_lda.html')

    print("Processing complete.")
