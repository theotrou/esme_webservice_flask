# Variables
PROJECT_NAME = flask_app
DOCKER_COMPOSE = docker-compose
PYTHON = python3

# Commandes pour l'application Flask
run:
	@echo "🚀 Lancement de l'application Flask..."
	$(PYTHON) app.py

install:
	@echo "📦 Installation des dépendances..."
	pip install -r requirements.txt

venv:
	@echo "🐍 Création d'un environnement virtuel..."
	python3 -m venv venv && source venv/bin/activate

clean:
	@echo "🧹 Nettoyage du projet..."
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf venv
	rm -rf .pytest_cache

# Commandes pour Docker
docker-build:
	@echo "🐳 Construction des conteneurs..."
	$(DOCKER_COMPOSE) up --build -d

docker-up:
	@echo "📦 Démarrage des conteneurs..."
	$(DOCKER_COMPOSE) up -d

docker-down:
	@echo "🛑 Arrêt et suppression des conteneurs..."
	$(DOCKER_COMPOSE) down

docker-clean:
	@echo "🧹 Nettoyage des images Docker..."
	docker system prune -af

# Commandes pour la base de données
db-init:
	@echo "📊 Initialisation de la base de données..."
	$(PYTHON) -c "from app import db; db.create_all()"

db-reset:
	@echo "🔄 Réinitialisation de la base de données..."
	$(PYTHON) -c "from app import db; db.drop_all(); db.create_all()"

# Aide
help:
	@echo "💡 Liste des commandes disponibles :"
	@echo "  make run            -> Lancer l'application Flask"
	@echo "  make install        -> Installer les dépendances Python"
	@echo "  make venv           -> Créer un environnement virtuel"
	@echo "  make clean          -> Nettoyer les fichiers temporaires"
	@echo "  make docker-build   -> Construire les conteneurs Docker"
	@echo "  make docker-up      -> Démarrer l'application avec Docker"
	@echo "  make docker-down    -> Arrêter et supprimer les conteneurs"
	@echo "  make docker-clean   -> Nettoyer les images Docker inutilisées"
	@echo "  make db-init        -> Créer les tables de la base de données"
	@echo "  make db-reset       -> Réinitialiser la base de données"
	@echo "  make help           -> Afficher cette aide"
