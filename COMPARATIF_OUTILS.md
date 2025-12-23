# 🔧 COMPARATIF DES OUTILS (Mission 4)

Objectif : Comparer les outils DevOps / QA utilisés dans les pipelines CI/CD.

---

## 🎨 **1. Linters Python**

| Outil   | Catégorie | Avantages | Inconvénients | Note /10 | Choix ? |
|---------|-----------|-----------|----------------|----------|---------|
| **Ruff** | Linter | Ultra rapide, écrit en Rust ; couvre Flake8 + isort + pyupgrade ; configuration simple | Moins exhaustif que Pylint sur l’analyse profonde | **9/10** | ✅ |
| **Flake8** | Linter | Standard classique, très extensible via plugins | Lent avec beaucoup de plugins ; règles limitées vs Ruff | 7/10 | ❌ |
| **Pylint** | Linter | Analyse très complète ; scoring du code ; excellent pour projets complexes | Lent ; parfois trop strict ; beaucoup de faux positifs | 6.5/10 | ❌ |

---

## 🎨 **2. Formatters Python**

| Outil | Catégorie | Avantages | Inconvénients | Note /10 | Choix ? |
|--------|-----------|-----------|---------------|----------|---------|
| **Ruff format** | Formatter | Très rapide ; compatible Black ; intégré au même outil que le linter | Encore jeune ; moins personnalisable | **9/10** | ✅ |
| **Black** | Formatter | Très adopté ; formatage cohérent et universel | Peu personnalisable ; plus lent que Ruff | 8/10 | ❌ |
| **autopep8** | Formatter | Simple, personnalisable | Peut produire un style non homogène ; adoption faible aujourd’hui | 6.5/10 | ❌ |

---

## 🔒 **3. Type Checkers**

| Outil | Catégorie | Avantages | Inconvénients | Note /10 | Choix ? |
|--------|-----------|-----------|---------------|----------|---------|
| **Mypy** | Type checker | Référence historique ; très précis | Parfois trop strict ; erreurs difficiles à lire | 8.5/10 | ❌ |
| **Pyright** | Type checker | Ultra rapide ; intégré VS Code ; messages clairs | Quelques limites avancées | **9.5/10** | ✅ |
| **Pyre** | Type checker | Rapide ; bien pour énormes codebases | Communauté réduite ; doc limitée | 7/10 | ❌ |

---

## 🧪 **4. Frameworks de Tests**

| Outil | Catégorie | Avantages | Inconvénients | Note /10 | Choix ? |
|--------|-----------|-----------|---------------|----------|---------|
| **pytest** | Test | Flexible ; fixtures puissantes ; riche écosystème | Peut devenir complexe avec trop de plugins | **9.5/10** | ✅ |
| **unittest** | Test | Inclus dans Python ; stable | Verbeux ; rigidité ; peu d’extensions | 7/10 | ❌ |

---

## 🔐 **5. Security Scanners**

| Outil | Catégorie | Avantages | Inconvénients | Note /10 | Choix ? |
|--------|-----------|-----------|---------------|----------|---------|
| **Bandit** | SAST Python | Analyse statique ciblée Python ; simple | Ne scanne pas les dépendances | 8/10 | ❌ |
| **Safety** | Vulnerabilities | Détecte failles des dépendances ; base fiable | Ne couvre pas le code | **9/10** | ✅ |
| **Snyk** | SCA + SAST | Complet ; UI ; intégré CI | Payant pour le full | 8.5/10 | ❌ |
| **Trivy** | Containers + deps | Scanne images Docker + système | Peut être lent si grosses images | **9/10** | ✅ |

---

## 🏆 Conclusion des choix recommandés

| Besoin | Outil recommandé |
|--------|------------------|
| Linter | **Ruff** |
| Formatter | **Ruff format** |
| Type checker | **Pyright** |
| Tests | **pytest** |
| Vulnerabilités deps | **Safety** |
| Scan containers | **Trivy** |

---
