# Daily Tasks

Léger gestionnaire de taches journalières

## Fonctionnalités en cours

1. Créer une tâche avec un identifiant, un titre, un statut et une date de création.
2. Enregistrer et charger les tâches depuis `daily_tasks/datas/tasks.json`.
3. Afficher une tâche à partir de son identifiant.
4. Marquer une tâche comme terminée.
5. Supprimer une tâche.

> Le projet est en cours d'apprentissage et de développement. Le menu interactif et certains affichages restent à finaliser.

## Prérequis

1. Python 3.13 ou une version plus récente.
2. [uv](https://docs.astral.sh/uv/) pour créer et gérer l'environnement du projet.

## Installation

Depuis la racine du projet :

```powershell
uv sync
```

Cette commande crée ou met à jour l'environnement virtuel `.venv` à partir de `pyproject.toml` et `uv.lock`.

## Lancer l'application

```powershell
uv run python -m daily_tasks.app
```

La forme `python -m daily_tasks.app` est importante : elle lance `app.py` comme le module `daily_tasks.app`, ce qui permet aux imports comme `from daily_tasks.task import Tasks` de fonctionner.

## Structure du projet

```text
cli_tool/
├── daily_tasks/
│   ├── app.py             # main
│   ├── task.py            # Classe Tasks
│   ├── storage.py         # Chargement et sauvegarde JSON
│   └── datas/
│       └── tasks.json     # Données des tâches
├── pyproject.toml         # Dépendances déclarées
├── uv.lock                # Versions 
└── README.md
```

## Format des données

Chaque tâche est enregistrée sous cette forme dans `tasks.json` :

```json
{
    "id": 1,
    "title": "Lire un chapitre Python",
    "completed": false,
    "created_at": "2026-09-14 20:13:24"
}
```

## Prochaine étape

Remplacer les appels de test placés à la fin de `app.py` par un menu qui permet à l'utilisateur de choisir une action : ajouter, lister, afficher, terminer ou supprimer une tâche.
