## Tifanny et Fanny
### Narratives.

#### Explication des dossiers et fichiers.

**Trois corpus** :
- **le_monde** : catégorie "le monde" sur les 3 sites
- **quoc_phong** aka defense : mot clé recherché sur les 3 sites
- **nv_corpus** : corpus sur le mot "défense" mais en ajoutant un corpus français issus du même site (VNP et ND)

**scripts** :
- **scrap_urls**_nomSite permettent de scrap les urls de 500 articles par site.
  - J'ai dû faire plusieurs scripts car les sites n'ont pas le même HTML.
- **extract**_nomSite sont les scripts qui permettent d'extraire le contenu des articles et de les tokeniser avant d'en sortir la visualisation lda.
  - Pareil, il y en a un par site.
- **lda_generale** permet de faire la visualisation de tous les articles ensemble, pour pouvoir comparer.
- **tokenizer_vn** permet de tokenizer les articles.
- **vncorenlp_script** permet d'obtenir des treebanks. Il faut l'appliquer sur des textes non tokénisés.
- **S_V_COD.py** : permet d'extraire sujet, verbe et complément d'objet direct 
- **S_V_raison.py** : finalement nous ne l'avons pas utilisé car les résultats n'était pas satisfaisant mais permet d'extraire sujet + verbe + CCcause 
- **calcul.py** : permet de faciliter le traitement des fichiers csv de sortie. 
- **dependencies.py** : permet de parser et d'extraire la structure : suj+verbe+cod.

**txt** :
- **urls**_nomSite sont les fichiers d'urls créées par les scripts **scrap_urls**.
  - ce sont ces fichiers qui sont ensuite utilisés en input pour **extract**.
- fichier de stopwords pour filtrer les mots.

**output** :
comme son nom l'indique, permet de stocker les outputs par site. les dossiers "notoken" sont les articles sans tokenisation et servent au VNCoreNLP
- **vncorenlp** est le dossier qui contient les articles qui sont passés sous vncorenlp

