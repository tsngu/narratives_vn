# Analyse syntaxique 

1. Démarche global : 

Nous souhaitons faire une analyse contrastive entre ces sites pour confronter la narrative sur une presse "libre" au vietnam. Est-ce que les seules ressources disponibles prouvent qu'il existe une pluralité idéologique de la presse ? Est-ce que l'on retrouve des formes de discours, des récurrences ? Celles-ci appuient-elles notre travail initial de recherche ? 

2. Le corpus : 

On utilise le même corpus pour toutes les analyses. Nous sommes allées scrapper sur 3 sites vietnamiens des articles de la catégorie International. Notre corpus est constitué d'environ 500 articles par site. 


3. Quels sont les patterns que l'on s'attends à rencontrer ? Pourquoi cette démarche ? 

L'analyse syntaxique consiste à mettre en évidence la structure d'un texte, généralement une phrase écrite dans une langue naturelle. 
Dans la phrase syntaxique, que l'on considère comme une unité de sens, on retrouve 2 constituants obligatoires : le sujet et le prédicat. On peut également retrouver un troisième constituant : le complément de phrase. 
Pour déterminer le nombre de phrase syntaxique il faut compter le nombre de verbe conjugué. (Premier traitement à faire ?) 
Dans la grammaire vietnamienne la construction de la phrase est la même qu'en français. 
On peut aussi regarder les phrases annotées comme passives ? 

3. Quels sont les outils que l'on utilise pour mettre en évidence les patterns syntaxiques ? 

On utilise dans un premier temps un annotateur qui nous permet d'annoter syntaxiquement les phrases. 
Pour ce faire, on utilise l'outil : VnCoreNLP 
Une fois que le texte est annoté, il faut réflechir à comment on peut mettre en avant les différentes structures. 
Les annotations sont dans un fichier .pdf dans le même dossier que ce document. 

Une fois cette annotation réalisée, nous obtenons un fichier txt que l'on process avec différents scripts python qui nous permettent d'extraire des patterns. 

Sous les conseils de Monsieur Valette, nous avons tenté d'utiliser TXM. Pour ce faire nous avons convertis nos sorties de fichiers txt (après le traitement avec vncorenlp) en fichier xml. Mais nous n'avons pas réussi à faire en sorte qu'il soit pris en charge par le logiciel. Ainsi, une piste d'amélioration pour notre travail serait de générer un fichier XML qui serait pris en charge par TXM pour faciliter les analyses.
En revanche, le compte-rendu de notre travail actuel nous permets dors et déjà de constater des résultats significatifs sur les procédés syntaxiques volontairement (ou non) utilisés dans la presse vietnamienne ont comme influence sur les narratives. 

Dans un soucis de traitement égalitaire, nous avons, malgré les outils existant pour le français, choisi de le traiter avec des outils similaires et en recherchant les mêmes patterns. 

4. Premiers résultats 

Pour la première recherche, je veux identifier les sujets et le COD qui leur est associé pour mettre en evidence leur position. 
J'essaye dans un premier temps sur quatre url. Une fois les résultats dans un fichier csv, je produis et execute un script qui me permet de mettre en valeur les combinaisons qui apparaissent le plus. 
Ce test sur quelques url nous pousse à nous interroger sur la généralisation de ces outils semi-automatiques qui rendent l'analyse pénible et coûteuse. De même, est-ce que nos machines seront capable de supporter 

5. Résultats sur notre corpus (français et vietnamien) 



6. Limites de notre étude

Notre travail d'analyse rencontre plusieurs problèmes méthodologiques majeurs qu'il est important de signaler. 
Tout d'abord notre corpus n'est pas parfaitement équilibré puisque certains sites sont équipés de pare-feu ce qui nous empêche d'avoir un corpus véritablement représentatif et équilibré. Ainsi les prémices de nos recherches seraient à confirmer en les transférant sur un corpus plus fiable. 
Et, étant limité dans l'utilisation de logiciels de textométris, nous avons exclusivement traité la syntage à l'aide de scripts python. Ce qui forcément oriente notre recherche et empêche en un sens de "laisser parler" le corpus. 
Malgré cela, nous pensons que notre étude garde une pertinence et qu'elle est encourageante pour des travaux futurs. Ce sujet de recherche mérite plus de temps et de moyens afin de vraiment "creuser" la question. 
