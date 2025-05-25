# 📊 Raydium API Data Analytics (Solana)

Ce projet a pour objectif de démontrer ma capacité à interagir avec une API REST, structurer des données financières issues de la blockchain Solana, et produire une première analyse à des fins exploratoires.

---

## 🔍 Objectifs

- Extraire les données des pools de liquidité sur [Raydium](https://raydium.io/)
- Transformer les données en DataFrame pour les analyser
- Visualiser les top pools selon la TVL (Total Value Locked)

---

## 🧠 Compétences démontrées

- Requête API (`requests`)
- Parsing de données JSON structurées
- Manipulation de données avec `pandas`
- Visualisation simple avec `matplotlib`
- Structuration d’un projet Python exploitable

---

## 📁 Description graphs

### 📊 Graphique 1 – Top 10 des pools par TVL (Total Value Locked)

Ce graphique présente les 10 pools de liquidité ayant la plus grande valeur totale.
	•	L’axe X affiche les noms des pools, c’est-à-dire les paires de tokens (ex : SLERF/WSOL, WSOL/USDC).
	•	L’axe Y indique la TVL, c’est-à-dire la valeur totale des deux tokens déposés, exprimée en dollars américains (USD).

💡 Interprétation :
Une TVL élevée reflète souvent un intérêt important pour un token, une forte activité de trading, ou une confiance élevée de la communauté envers la paire.
🕒 Remarque importante :
Les valeurs affichées correspondent à un instantané pris au moment de l’appel API.

### 📊 Graphique 2 – Paires avec les tokens au prix unitaire le plus élevé

Ce graphique présente les 10 pools dont l’un des tokens a le prix unitaire le plus élevé, selon les données extraites de l’API Raydium.

- L’axe **X** correspond aux **paires de tokens** (ex : `WSOL/Pnut`).
- L’axe **Y** indique le **prix unitaire** (en dollars) du token dans la paire concernée.

💡 **Interprétation :**  
> Un prix élevé peut refléter soit un **token très valorisé par le marché**, soit un token à **faible offre.  
> Ce graphique met en évidence les actifs qui possèdent la **valeur unitaire la plus élevée** sur la plateforme, même s’ils ne sont pas forcément les plus liquides ou les plus populaires.

### 📊 Graphique 3 – Tokens populaires à prix bas (TVL élevée + prix faible)

Ce graphique met en évidence les tokens qui cumulent une **valeur unitaire faible** (moins de 0.01 $) et une **TVL élevée** (plus de 1 million de dollars).  
Ces tokens sont souvent **accessibles au grand public**, fortement échangés, voire alimentés par des communautés actives.

💡 **Interprétation :**  
> Ce type de profil correspond souvent à des **memecoins, shitcoins, qui peuvent représenter un fort potentiel spéculatif… mais aussi un niveau de risque élevé.
📌 À propos du seuil de 1M $ de TVL : seuil minimum de TVL à 1 million de dollars** pour ne conserver que les pools présentant une liquidité significative.  
Cela permet de filtrer :
- Les pools peu actifs ou récents
- Les tokens ayant peu d’engagement réel sur la plateforme