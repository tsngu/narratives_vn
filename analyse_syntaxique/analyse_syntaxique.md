# Analyse syntaxique 

### 1. Démarche globale : 

Nous souhaitons faire une analyse contrastive entre ces sites pour confronter la narrative sur une presse "libre" au vietnam. Est-ce que les seules ressources disponibles prouvent qu'il existe une pluralité idéologique de la presse ? Est-ce que nous retrouvons des formes de discours, des récurrences ? Celles-ci appuient-elles notre travail initial de recherche ? 

Notre recherche est au-delà d'une simple analyse syntaxique. En effet, elle tend plutôt à s'inscrire dans une analyse du discours. Celle-ci ne considère pas ce corpus comme un support d'information mais bien comme nous avons tenté de le démontrer dans notre premier devoir est plutôt de considérer ce corpus et chacun des textes qui le composent comme un *texte*. 
Ainsi, notre étude cherche à être sémiologique. En effet, notre première partie consistait à définir les "lois qui régissent l'univers raconté" (Claude Bremond, La logique des possibles narratifs)c'est à dire le contexte politique et médiatique de la presse vietnamienne sur internet et dans un second temps, celui du présent devoir qui est "l'analyse techniques de narration" que nous essayons de faire à l'aide d'une analyse du discours. 

### 2. Le corpus : 

Contrairement au premier semestre, nous avons travaillé sur deux corpus différents :

Le premier est constitué de 3 sites vietnamiens (disponible à l'international) : Nhan Dan, Vietnam Plus et Bao Tin Tuc. Nous avons scrap 500 articles par site en utilisant le mot clé "Quoc phong", c'est-à-dire "Défense". 

A l'avant dernière séance, Mr. Valette nous a parlé de faire plutôt une comparaison avec un corpus français.
Nous avons donc constitué un nouveau corpus pour avoir des articles à des dates similaires. Ce fût un semi-échec : Bao Tin Tuc n'a pas de version française et Nhan Dan bloque le scraping à 30 URLs sur le site français. Nous n'avons pas eu le temps de trouver une méthode pour contourner ça. Nous sommes donc ressorti avec un corpus déséquilibré : le corpus Nhan Dan est composé de 525 articles vietnamien mais seulement 30 français. Par contre, pour VietnamPlus, tout a marché : nous avons donc 500 articles vietnamiens et 500 articles français.

### 3. Rappel premier semestre :

Au premier semestre, nous avions fait une analyse LDA au corpus constitué des trois sites. Nous avons refait la même chose sur le nouveau corpus.
Pour le corpus VNP, en vietnamien, les 5 mots qui ressortent le plus sont les suivants :
- Điện Biên Phủ : le nom d'une ville
- phát triển : (se) développer
- hợp tác : coopérer, collaborer
- chiến thắng : victorieux
- quốc phòng : défense nationale

en français, ce sont les suivants :
- défense
- Laos
- Dien Bien
- industrie
- sécurité

Pour le corpus ND, les résultats étaient les suivants :
- quốc phòng : défense nationale
- Viet Nam
- hợp tác : coopérer, collaborer
- cơ_quan : établissement
- xây dựng : batir, construire*

et pour le français :
- Vietnam
- Coopération
- Défense
- paix
- Chine

Ces résultats montrent que même en France, les articles sont portés vers la "coopération internationale" pour la "paix" et la "sécurité" du pays.

### 4. Quels sont les patterns auxquels nous nous attendons à rencontrer ? Pourquoi cette démarche ? 

L'analyse syntaxique consiste à mettre en évidence la structure d'un texte, généralement une phrase écrite dans une langue naturelle. 
Dans la phrase syntaxique, que nous considérons comme une unité de sens, nous retrouvons 2 constituants obligatoires : le sujet et le prédicat. Nous pouvons également retrouver un troisième constituant : le complément de phrase. 
Pour déterminer le nombre de phrase syntaxique il faut compter le nombre de verbe conjugué. (Premier traitement à faire ?) 
Dans la grammaire vietnamienne la construction de la phrase est la même qu'en français. 
Nous pouvons aussi regarder les phrases annotées comme passives ? 

### 5. Quels sont les outils que nous utilisons pour mettre en évidence les patterns syntaxiques ? 

Nous utilisons dans un premier temps un annotateur qui nous permet d'annoter syntaxiquement les phrases. 
Pour ce faire, nous utilisons l'outil : VnCoreNLP 
Une fois que le texte est annoté, il faut réflechir à comment nous pouvons mettre en avant les différentes structures. 
Les annotations sont dans un fichier .pdf dans le même dossier que ce document. 

Une fois cette annotation réalisée, nous obtenons un fichier txt que nous processons avec différents scripts python qui nous permettent d'extraire des patterns. 

Sous les conseils de Monsieur Valette, nous avons tenté d'utiliser TXM. Pour ce faire nous avons convertis nos sorties de fichiers txt (après le traitement avec vncorenlp) en fichier xml. Mais nous n'avons pas réussi à faire en sorte qu'il soit pris en charge par le logiciel. Ainsi, une piste d'amélioration pour notre travail serait de générer un fichier XML qui serait pris en charge par TXM pour faciliter les analyses.
En revanche, le compte-rendu de notre travail actuel nous permets dors et déjà de constater des résultats significatifs sur les procédés syntaxiques volontairement (ou non) utilisés dans la presse vietnamienne ont comme influence sur les narratives. 

Dans un soucis de traitement égalitaire, nous avons, malgré les outils existant pour le français, choisi de le traiter avec des outils similaires et en recherchant les mêmes patterns. 

### 6. Premiers résultats 

Pour la première recherche, je veux identifier les sujets et le COD qui leur est associé pour mettre en evidence leur position. 
J'essaye dans un premier temps sur quatre urls. Une fois les résultats dans un fichier csv, je produis et execute un script qui me permet de mettre en valeur les combinaisons qui apparaissent le plus. 
Ce test sur quelques urls nous pousse à nous interroger sur la généralisation de ces outils semi-automatiques qui rendent l'analyse pénible et coûteuse. De même, est-ce que nos machines seront capable de supporter 

### 7. Résultats sur notre corpus (français et vietnamien) 



### 8. Limites de notre étude

Notre travail d'analyse rencontre plusieurs problèmes méthodologiques majeurs qu'il est important de signaler. 
Tout d'abord notre corpus n'est pas parfaitement équilibré puisque certains sites sont équipés de pare-feu ce qui nous empêche d'avoir un corpus véritablement représentatif et équilibré. Ainsi les prémices de nos recherches seraient à confirmer en les transférant sur un corpus plus fiable. 
Et, étant limité dans l'utilisation de logiciels de textométris, nous avons exclusivement traité la syntage à l'aide de scripts python. Ce qui forcément oriente notre recherche et empêche en un sens de "laisser parler" le corpus. 
Malgré cela, nous pensons que notre étude garde une pertinence et qu'elle est encourageante pour des travaux futurs. Ce sujet de recherche mérite plus de temps et de moyens afin de vraiment "creuser" la question. 


### Bibliographie 

Communications, 8, 1966. Recherches sémiologiques : L'analyse structurale du récit (https://www.persee.fr/issue/comm_0588-8018_1966_num_8_1) 
L'analyse française du discours (https://shs.hal.science/file/index/docid/396398/filename/index.html) 

