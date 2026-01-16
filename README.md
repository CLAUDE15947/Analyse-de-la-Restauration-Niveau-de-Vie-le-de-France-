Analyse de la restauration en Île-de-France
J'ai réalisé ce projet pour comprendre comment le niveau de vie des communes influence le secteur de la restauration. L'idée était de voir s'il existe une corrélation réelle entre la richesse d'une ville (revenu, chômage, éducation) et les caractéristiques de ses restaurants (prix, notes, popularité).


 Ce que j'ai fait :

Récupération des données : J'ai scrapé environ 10 000 restaurants sur RestaurantGuru.



Enrichissement API : Comme le scraping ne donnait pas les communes précises, j'ai utilisé l'API Nominatim pour transformer les coordonnées GPS en codes INSEE.



Analyse & Nettoyage : J'ai nettoyé les datasets et agrégé les données socio-économiques de l'INSEE avec les données des restaurants.


Machine Learning : J'ai développé un modèle de Gradient Boosting pour prédire le prix moyen d'un restaurant en fonction de sa localisation et de sa catégorie.

📈 Résultats techniques
Pour la partie prédiction, j'ai utilisé GridSearchCV pour optimiser mon modèle et appliqué une transformation logarithmique sur les prix pour obtenir des résultats plus précis. Le projet inclut aussi une structure SQL pour stocker proprement les données finales.
