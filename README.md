## Tifanny et Fanny
### Narratives.

#### Explication des dossiers et fichiers.

**Deux corpus** :
- **le_monde** : catégorie "le monde" sur les 3 sites
- **quoc_phong** aka defense : mot clé recherché sur les 3 sites

**scripts** :
- **scrap_urls**_nomSite permettent de scrap les urls de 500 articles par site.
  - J'ai dû faire plusieurs scripts car les sites n'ont pas le même HTML.
- **extract**_nomSite sont les scripts qui permettent d'extraire le contenu des articles et de les tokeniser avant d'en sortir la visualisation lda.
  - Pareil, il y en a un par site.
- **lda_generale** permet de faire la visualisation de tous les articles ensemble, pour pouvoir comparer.
- **tokenizer_vn** permet de tokenizer les articles.
- **vncorenlp_script** permet d'obtenir des treebanks. Il faut l'appliquer sur des textes non tokénisés.

**txt** :
- **urls**_nomSite sont les fichiers d'urls créées par les scripts **scrap_urls**.
  - ce sont ces fichiers qui sont ensuite utilisés en input pour **extract**.
- fichier de stopwords pour filtrer les mots.

**output** :
comme son nom l'indique, permet de stocker les outputs par site. les dossiers "notoken" sont les articles sans tokenisation et servent au VNCoreNLP
- **vncorenlp** est le dossier qui contient les articles qui sont passés sous vncorenlp

