# Flask Books API

## 🚀 Installation & Exécution

### 📌 Prérequis
- **Windows** : Installer [Python](https://www.python.org/downloads/), [Docker Desktop](https://www.docker.com/products/docker-desktop/) et [Make for Windows](http://gnuwin32.sourceforge.net/packages/make.htm) 
- **Linux / Mac** : Avoir `python3`, `pip`, `docker`, `docker-compose`, et `make` installés

### 🏗️ Installation des dépendances
#### 1️⃣ Cloner le projet
```bash
git clone git@github.com:esperluet/esme_webservice_flask.git
cd esme_webservice_flask
```

#### 2️⃣ Installer les dépendances Python
```bash
make install
```

#### 3️⃣ (Optionnel) Créer un environnement virtuel
```bash
make venv
```

### 🏃‍♂️ Lancer l'application Flask
```bash
make run
```
L'API sera accessible à `http://localhost:5000`.

### 🐳 Démarrer l’application avec Docker
```bash
make docker-build
```
Pour arrêter l’application :
```bash
make docker-down
```

## 📚 API Endpoints

### 🔹 Récupérer tous les livres
```http
GET /books
```

### 🔹 Ajouter un livre
```http
POST /books
Content-Type: application/json
{
  "title": "Le Petit Prince",
  "author": "Antoine de Saint-Exupéry",
  "published_at": "1943-04-06"
}
```

### 🔹 Récupérer un livre spécifique
```http
GET /books/1
```

### 🔹 Mettre à jour un livre
```http
PUT /books/1
Content-Type: application/json
{
  "title": "Le Petit Prince (Édition spéciale)",
  "published_at": "1943-04-07"
}
```

### 🔹 Supprimer un livre
```http
DELETE /books/1
```

## 🛠 Commandes utiles

| Commande | Description |
|----------|------------|
| `make install` | Installe les dépendances Python |
| `make venv` | Crée un environnement virtuel |
| `make run` | Démarre l'application Flask |
| `make clean` | Supprime les fichiers temporaires |
| `make docker-build` | Construit et démarre les conteneurs Docker |
| `make docker-up` | Démarre l'application avec Docker |
| `make docker-down` | Arrête et supprime les conteneurs |
| `make docker-clean` | Supprime les images Docker inutilisées |
| `make db-init` | Initialise la base de données (crée les tables) |
| `make db-reset` | Réinitialise la base de données (supprime et recrée les tables) |
| `make help` | Affiche la liste des commandes disponibles |

## 🛠 Technologies utilisées
- **Flask** (Backend en Python)
- **PostgreSQL** (Base de données)
- **Docker & Docker Compose** (Déploiement et conteneurisation)
- **Makefile** (Gestion automatisée des tâches)