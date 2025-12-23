### 📝 Missions de veille

#### **Mission 1 : Comprendre CI/CD (1h)**

**Ressources obligatoires** :
- 📖 [Red Hat - Qu'est-ce que la CI/CD ?](https://www.redhat.com/fr/topics/devops/what-is-ci-cd)
- 🎥 [GitHub Actions Tutorial](https://www.youtube.com/watch?v=R8_veQiYBjI) (30min)

---

### ✅ **Questions à documenter**

---

## **1️⃣ Qu'est-ce que la CI (Continuous Integration) ?**

### **🔍 Définition**
La **CI** est une pratique DevOps où les développeurs intègrent fréquemment leur code dans un dépôt partagé. Chaque intégration déclenche des build et des tests automatiques.

### **🎯 Problèmes résolus**
- Réduction des conflits d’intégration
- Détection rapide des bugs
- Build automatisés → moins d’erreurs humaines
- Amélioration de la stabilité du code

### **🧩 Principes clés**
- Intégrer souvent (plusieurs fois par jour)
- Automatiser les tests et le build
- Maintenir une branche principale stable
- Fournir un feedback rapide aux développeurs

### **🛠️ Exemples d’outils CI**
- **GitHub Actions**
- **Jenkins**
- **GitLab CI/CD**

---

## **2️⃣ Qu'est-ce que le CD (Continuous Delivery / Continuous Deployment) ?**

### **🔍 Définition**
Le **CD** automate les étapes après la CI : tests avancés, packaging, déploiement jusqu’aux environnements de production ou pré-production.

### **🚀 Continuous Delivery vs Continuous Deployment**
| Continuous Delivery | Continuous Deployment |
|---------------------|------------------------|
| Le déploiement en production est **manuel** | Le déploiement en production est **automatique** |
| L'équipe valide avant mise en prod | Toute modification validée est déployée |
| Plus prudent, plus contrôlé | Plus rapide, nécessite une confiance totale dans les tests |

### **⚖️ Bénéfices**
- Déploiements plus rapides
- Réduction des risques (petites modifications fréquentes)
- Automatisation des processus → moins d’erreurs

### **⚠️ Risques**
- Mauvaise qualité des tests → bugs en production
- Pipeline mal configuré → interruptions possibles
- Nécessite une culture DevOps solide

---

## **3️⃣ Pourquoi CI/CD est important ?**

### **💡 Impact sur la qualité du code**
- Tests automatisés → moins de régressions
- Intégration fréquente → code plus propre
- Feedback instantané aux développeurs

### **⚡ Impact sur la vitesse de développement**
- Moins d’attente entre les étapes
- Déploiements rapides et fiables
- Livraison continue de nouvelles fonctionnalités

### **🤝 Impact sur la collaboration en équipe**
- Standardisation du workflow
- Moins de conflits entre branches
- Transparence et communication fluide
- Travail aligné grâce aux pipelines automatisés

### 🧪 Mission 2 : Maîtriser **uv** (1h)

**Ressources obligatoires** :
- 📖 Documentation officielle uv
- 📖 uv – GitHub Integration
- 📖 uv – Build Backend
- 🎥 uv Tutorial

---

## 1️⃣ Qu'est-ce que **uv** ?

### 🔍 Définition

**uv** est un outil tout‑en‑un pour l’écosystème Python qui combine plusieurs rôles :

- gestionnaire de dépendances
- gestionnaire d’environnements virtuels
- outil d’exécution de commandes (scripts, tests, etc.)
- backend de build pour les projets Python modernes

Il s’appuie fortement sur **pyproject.toml** et vise à être **rapide**, **reproductible** et simple à intégrer dans des workflows automatisés (CI/CD).

---

### 🆚 Différences avec pip / poetry / pipenv

| Outil      | Rôle principal                                      | Points clés |
|-----------|------------------------------------------------------|------------|
| **pip**   | Installer des paquets à partir de PyPI              | Gère les paquets mais pas les environnements ni le lock par défaut |
| **pipenv**| Gestion dépendances + environnements virtualenv      | Crée un `Pipfile` et des venvs automatiquement |
| **poetry**| Gestion complète des projets et dépendances          | Utilise `pyproject.toml`, gère versions, build et publication |
| **uv**    | Gestionnaire **polyvalent** et ultra rapide          | Combine gestion de deps, environnements, exécution & build backend via `pyproject.toml` |

En résumé :
- **pip** = installation “de base”
- **poetry/pipenv** = gestion de projet haut niveau
- **uv** = approche moderne, unifiée, orientée performance et CI/CD.

---

### ✅ Avantages de uv

- **Performance** : installation et résolution de dépendances très rapides.
- **Approche unifiée** : un seul outil pour gérer :
  - dépendances
  - environnements
  - commandes (tests, lint, scripts)
  - build backend
- **Intégration moderne** :
  - basé sur `pyproject.toml`
  - bien adapté aux pipelines CI/CD
- **Reproductibilité** :
  - gestion de fichiers de lock
  - versions figées pour avoir le même environnement en local et en CI.

---

## 2️⃣ Comment uv fonctionne avec `pyproject.toml` ?

### 🧱 Structure du fichier

`pyproject.toml` est le fichier central de configuration du projet. Avec **uv**, on y trouve typiquement :

```toml
[project]
name = "mon-projet"
version = "0.1.0"
description = "Exemple de projet avec uv"
readme = "README.md"
requires-python = ">=3.10"

[project.dependencies]
# dépendances principales
numpy = "^1.26"
pydantic = "^2.0"

[project.optional-dependencies]
dev = [
  "pytest",
  "ruff",
]

[build-system]
requires = ["uv"]
build-backend = "uv.build"
```

> La syntaxe exacte peut varier, mais l’idée est : **uv lit et gère tout via `pyproject.toml`**.

---

### 📦 Gestion des dépendances (sections)

- `[project.dependencies]` : dépendances **runtime** utilisées par l’application.
- `[project.optional-dependencies]` : groupes de dépendances (ex : `dev`, `test`, `docs`).
- uv permet d’installer :
  - seulement les dépendances de base
  - ou un groupe (ex : `dev`) pour le développement.

Exemple de commandes (style général) :

```bash
uv add numpy
uv add pytest --group dev
```

---

### 🏗️ Build backend avec uv

Dans la section `[build-system]` :

```toml
[build-system]
requires = ["uv"]
build-backend = "uv.build"
```

Cela signifie que :

- **uv** est utilisé pour construire le paquet (wheel, sdist, etc.)
- les commandes de build (ex : dans CI/CD) utilisent uv comme moteur unifié.

Avantages :

- configuration centralisée
- build cohérent entre local et CI
- moins de dépendances externes (pas besoin de `setuptools` + `wheel` + autre outil).

---

## 3️⃣ Comment utiliser uv dans GitHub Actions ?

### ⚙️ Installation de uv

Dans un workflow GitHub Actions, on ajoute une étape d’installation, par exemple :

```yaml
- name: Install uv
  run: |
    curl -LsSf https://astral.sh/uv/install.sh | sh
```

ou via un binaire déjà fourni selon la doc officielle.

---

### 🗄️ Cache des dépendances

Pour accélérer les workflows CI, on met en cache :

- le **répertoire de cache** de uv
- ou le **fichier de lock** associé aux dépendances.

Exemple (générique) :

```yaml
- name: Cache uv
  uses: actions/cache@v4
  with:
    path: ~/.cache/uv
    key: ${{ runner.os }}-uv-${{ hashFiles('pyproject.toml') }}
```

Ainsi, si `pyproject.toml` n’a pas changé, les dépendances ne seront pas réinstallées depuis zéro.

---

### ▶️ Exécution de commandes avec uv

Une fois uv installé et le cache configuré, on peut :

1. Installer les dépendances :

```yaml
- name: Install dependencies
  run: uv sync
```

2. Exécuter des commandes (tests, lint, etc.) :

```yaml
- name: Run tests
  run: uv run pytest
```

3. Construire le paquet (build backend) :

```yaml
- name: Build package
  run: uv build
```

---
### 🚀 Mission 3 : Comprendre Semantic Release (30min)

**Ressources obligatoires :**
- 📖 Conventional Commits
- 📖 Conventional Commits – Gist
- 📖 Python Semantic Release

---

## 1️⃣ Qu'est-ce que le versionnage sémantique (SemVer) ?

Le **versionnage sémantique** est une manière standardisée de numéroter les versions d’un logiciel suivant le format :

```
MAJOR.MINOR.PATCH
```

### 🔢 Signification

- **MAJOR** : changements incompatibles (breaking changes)
- **MINOR** : nouvelles fonctionnalités rétro-compatibles
- **PATCH** : corrections de bugs sans changement majeur ni ajout de fonctionnalités

### ⬆️ Quand bumper chaque niveau ?

| Type de changement | Exemple | Niveau |
|------------------|---------|--------|
| Rupture de compatibilité | suppression d’une API | MAJOR |
| Nouvelle fonctionnalité | ajout d’un endpoint | MINOR |
| Bugfix | correction d’un crash | PATCH |

---

## 2️⃣ Qu'est-ce que Conventional Commits ?

**Conventional Commits** définit un format structuré pour les messages Git afin d’automatiser le versionnage.

Format standard :

```
type(scope?): description
```

### 🎭 Types principaux

| Type       | Signification |
|------------|--------------|
| **feat**   | nouvelle fonctionnalité → bump MINOR |
| **fix**    | correction de bug → bump PATCH |
| **docs**   | documentation |
| **style**  | formatage, pas de logique |
| **refactor** | amélioration interne sans changement fonctionnel |
| **test**   | tests |
| **perf**   | optimisation |
| **ci** / **build** | pipeline, build system |

### 💥 Impact sur SemVer

- **feat** → MINOR
- **fix** → PATCH
- **BREAKING CHANGE** dans le corps → MAJOR

Exemple :

```
feat: add user authentication

BREAKING CHANGE: login endpoint renamed
```

Cela déclenche automatiquement un bump MAJOR.

---

## 3️⃣ Comment fonctionne python-semantic-release ?

**python-semantic-release** automatise :

1. le versionnage
2. la génération du changelog
3. la création des tags Git
4. la publication GitHub et PyPI

---

### 🛠️ Configuration dans `pyproject.toml`

Exemple minimal :

```toml
[tool.semantic_release]
version_variable = "package/__init__.py:__version__"
branch = "main"
changelog_file = "CHANGELOG.md"
upload_to_pypi = false
upload_to_release = true
build_command = "python -m build"
```

---

### 🧾 Génération du CHANGELOG

Semantic Release :

- lit l’historique Git
- détecte le type des commits
- regroupe les changements : feat, fix, breaking
- met à jour automatiquement `CHANGELOG.md`

Exemple de section :

```
## 1.4.0 - 2024-11-01

### Features
- Add loan predictor (feat)

### Fixes
- Correct environment variable loading (fix)
```

---

### 🏷️ Création des releases GitHub

Lorsqu'il est exécuté dans CI :

- crée automatiquement un **tag Git**
- crée un **GitHub Release**
- ajoute le changelog généré dans la release
- peut publier les artefacts (wheel, sdist) selon config

Workflow minimal :

```yaml
- name: Run Semantic Release
  run: semantic-release publish
```

---
