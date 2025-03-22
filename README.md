# Flask Books API

Ce projet est une API REST simple développée avec Flask pour gérer une collection de livres, utilisant PostgreSQL comme base de données et Docker pour faciliter la gestion des environnements.

---

## 🚀 Installation & Exécution

### 📌 Prérequis

**Recommandations d'outils complémentaires :**
- [Postman](https://www.postman.com/downloads/) pour tester les endpoints de l'API.
- [DBeaver](https://dbeaver.io/download/) pour visualiser la base de données.

#### 🖥️ Windows
- Installer [Python](https://www.python.org/downloads/)
- Installer [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Installer [Make for Windows (GnuWin32)](http://gnuwin32.sourceforge.net/packages/make.htm) ou utiliser [Chocolatey](https://chocolatey.org/install) : `choco install make`
- **Ajouter `make` dans le PATH système** pour pouvoir exécuter les commandes `make` dans un terminal (cmd ou PowerShell)

#### 🐧 Linux / 🍏 macOS
- Vérifier que `python3`, `pip`, `docker`, `docker-compose` et `make` sont installés

### 🏗️ Installation

#### 1️⃣ Cloner le projet
```bash
git clone git@github.com:esperluet/esme_webservice_flask.git
cd esme_webservice_flask
```

#### 2️⃣ Construire et démarrer l’application avec Docker
```bash
make docker-build
```

L'API sera accessible sur [http://localhost:5009](http://localhost:5009).

> **Note :** Si vous souhaitez uniquement démarrer l'application sans reconstruire l'image Docker :
> ```bash
> make docker-up
> ```

### 🐳 Pour arrêter l’application
```bash
make docker-down
```

> 📦 **Persistance des données** : Les données PostgreSQL sont stockées dans un volume Docker nommé `postgres_data`. Elles sont donc conservées même après l'arrêt ou la suppression du conteneur.
> 
> De plus, les fichiers de migration Alembic sont synchronisés avec le dossier local `./migrations/`, ce qui permet de conserver l'historique des migrations et de les versionner dans Git.

---

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
GET /books/<book_id>
```

### 🔹 Mettre à jour un livre
```http
PUT /books/<book_id>
Content-Type: application/json

{
  "title": "Le Petit Prince (Édition spéciale)",
  "published_at": "1943-04-07"
}
```

### 🔹 Supprimer un livre
```http
DELETE /books/<book_id>
```

---

## 🛠 Commandes utiles

| Commande             | Description                                              |
|----------------------|----------------------------------------------------------|
| `make docker-build`  | Construit et démarre les conteneurs Docker               |
| `make docker-up`     | Démarre les conteneurs existants                         |
| `make docker-down`   | Arrête et supprime les conteneurs                        |
| `make docker-clean`  | Nettoie les images Docker inutilisées                    |
| `make db-init`       | Initialise la base de données (crée les tables)          |
| `make db-migrate`    | Crée une migration à partir des modifications du modèle  |
| `make db-upgrade`    | Applique les migrations à la base de données             |
| `make db-reset`      | Réinitialise complètement la base de données             |
| `make help`          | Affiche toutes les commandes disponibles                 |

---

## 🛠 Technologies utilisées

- **Flask** : Framework web en Python pour la création de l'API REST.
- **PostgreSQL** : Base de données relationnelle pour le stockage des livres.
- **Docker & Docker Compose** : Gestion des environnements et conteneurisation.
- **Makefile** : Automatisation des commandes et simplification des tâches.

---

## ❗ Conseils supplémentaires pour les utilisateurs Windows

- Si la commande `make` n’est pas reconnue, ajoutez manuellement le dossier contenant `make.exe` à votre variable d’environnement `PATH`.
- Il est recommandé d’utiliser Git Bash, PowerShell ou WSL pour éviter les problèmes liés aux chemins ou à l'encodage des commandes dans le terminal.
- En cas d’erreur lors de l’exécution des commandes Makefile, vérifiez que Docker est bien lancé et que les conteneurs sont en cours d’exécution (`make docker-up`).
