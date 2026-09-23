# Daily Tasks

Léger gestionnaire de taches journalières

## Fonctionnalités en cours

1. Interface cli avec argparse + rich

> Le projet est en cours d'apprentissage et de développement. Le menu interactif et certains affichages restent à finaliser.

## Prérequis

1. Python 3.13 ou une version plus récente.
2. [uv](https://docs.astral.sh/uv/) pour créer et gérer l'environnement du projet.

## Installation

Depuis la racine du projet :

```powershell
uv sync
```

## Lancer l'application

```powershell
uv run python -m daily_tasks.app
```

## Liste des fonctions

- ajouter une tache : 
```python
uv run python -m daily_tasks.app add "my task"
```
- lister les taches :
```python
uv run python -m daily_tasks.app list_tasks()
```
- supprimer une tache :
```python
uv run python -m daily_tasks.app del [id]
```
- marquer comme complétée :
```python
uv run python -m daily_tasks.app done [id]
```
- afficher une tache :
```python
uv run python -m daily_tasks.app display [id]
```


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

Chaque tâche est enregistrée dans `tasks.json` :

```json
{
    "id": 1,
    "title": "Lire un chapitre Python",
    "completed": false,
    "created_at": "2026-09-14 20:13:24"
}
```

## Prochaine étape

- rich + pour l'interface CLI
- régulariser pour pouvoir lancer l'application


