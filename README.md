# ProjectFastAPI

Projet final du cours Développement web back - fullstack avec M. POISOT à EFFICOM en utilisant Fastapi et Python
C'est une application back-end permettant de "CRUD" des utilisateurs, entreprises, planning, acitités

## Documentation Swagger
La documentation est automatiquement disponible sur FQDN:port/docs/ ou /redoc
Le FQDN par défaut est localhost et le port par défaut est 80.

## Exécuteion de l'application
2 modes possibles pour lancer l'application, celui recommandé est le mode Docker.
Une fois lancée, l'application sera accessible à http://localhost sauf si vous utilisez ce port pour autre chose.

### Mode Docker
Prérequis : docker et docker-compose installés
Pour se lancer, votre terminal doit être à la racine de ce dossier.
Puis exécuter la commande suivane :
docker-compose up --build

### Mode Uvicorne
Prérequis : python3.10 ou supérieur installé
Tout d'abord, installez les dépendances:
pip install -r requirements.txt

Ensuite, lancez l'application :
uvicorn main:app --host 0.0.0.0 --port 80

## Authentification

## Base de données

Par défaut, la base de données est sqlite. 
Il est recommandé de l'utiliser avec des données testables.
Mais, vous pouvez toujours utiliser une autre base de données si vous le souhaitez.
La base de données se trouve dans le dossier /app et son nom par défaut est fastapi.db.

### Modèle Entité Association (MEA)

![](public/assets/bdd.png)

### Concepteur de la base de données

![](public/assets/concept.png)

