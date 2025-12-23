# Veille technologique — Observabilité & Monitoring

## 1. Contexte

Dans un contexte DevOps et CI/CD, l’observabilité est un pilier essentiel pour garantir la fiabilité, la performance et la maintenabilité des applications.  
Ce projet s’inscrit dans une démarche complète d’observabilité appliquée à une API Python développée avec FastAPI.

L’objectif est de surveiller :
- l’état de santé de l’application
- ses performances
- son comportement sous charge
- la qualité du pipeline CI/CD

---

## 2. Différence entre Monitoring et Observabilité

### Monitoring
Le monitoring consiste à **surveiller des métriques connues** :
- disponibilité d’un service
- taux d’erreurs
- temps de réponse
- consommation de ressources

Il répond principalement à la question :
> *“Est-ce que le système fonctionne ?”*

### Observabilité
L’observabilité va plus loin :  
elle permet de **comprendre pourquoi un système se comporte d’une certaine manière**, même en cas de problème inconnu.

Elle repose sur trois piliers :
- **Metrics** : données chiffrées (latence, taux de requêtes, erreurs)
- **Logs** : événements détaillés
- **Traces** : parcours des requêtes dans le système

---

## 3. Outils étudiés

### Prometheus
Prometheus est un outil open-source de collecte de métriques.
Il fonctionne par scrapping et est particulièrement adapté aux architectures microservices.

Dans ce projet, Prometheus est utilisé pour :
- collecter les métriques exposées par l’API FastAPI
- stocker les données de performance
- servir de source de données pour Grafana

### Grafana
Grafana est un outil de visualisation de données.
Il permet de créer des tableaux de bord dynamiques à partir de différentes sources (Prometheus, Loki, etc.).

Dans ce projet, Grafana est utilisé pour :
- visualiser le nombre de requêtes par endpoint
- analyser les temps de réponse
- observer l’évolution de la charge applicative

### prometheus-fastapi-instrumentator
Cette librairie permet d’instrumenter automatiquement une application FastAPI.
Elle expose des métriques standards compatibles avec Prometheus, telles que :
- nombre de requêtes HTTP
- latence des endpoints
- codes de réponse

---

## 4. Observabilité dans le pipeline CI/CD

Le pipeline CI/CD intègre plusieurs niveaux de contrôle :

- **Linting (Ruff)** : qualité du code
- **Type checking (Mypy)** : robustesse des types
- **Tests unitaires (Pytest)** : validation fonctionnelle
- **Sécurité (Bandit, Safety, detect-secrets)** : prévention des failles
- **Pre-commit en CI** : garantie que les règles locales ne sont pas contournées

Ces étapes permettent de détecter les problèmes **avant le déploiement**, ce qui renforce la fiabilité globale du système.

---

## 5. Cas d’usage concrets

Grâce à l’observabilité mise en place, il est possible de :
- détecter un endpoint lent ou surchargé
- analyser une augmentation anormale des erreurs HTTP
- vérifier l’impact d’une nouvelle version de l’application
- anticiper les problèmes de performance

---

## 6. Conclusion

L’observabilité est aujourd’hui indispensable pour toute application moderne.
Ce projet démontre la mise en œuvre concrète d’un système d’observabilité complet, combinant :
- instrumentation applicative
- collecte de métriques
- visualisation
- intégration CI/CD

Cette approche permet d’améliorer la qualité, la résilience et la maintenabilité de l’application sur le long terme.
