# Daily Tasks

Léger gestionnaire de taches journalières


## Requirements

1. Python 3.13 ou une version plus récente.
2. [uv](https://docs.astral.sh/uv/) pour créer et gérer l'environnement du projet.

## Installation

Depuis la racine du projet :

```powershell
uv sync
```

## Lancer l'application en mode interactif

```powershell
uv run python -m daily_tasks.app
```
### Commandes
```powershell
# aide
❯ help

# ajouter un tache d'id [id]
❯ add Acheter du pain

# lister les taches
❯ list

# marquer une tache d'id [id] comme lue
❯ done 1

# afficher une tache spécifique d'id [id]
❯ display 1

# supprimer une tache d'id [id]
daily-tasks ❯ del 2

# effacer l'affichage
❯ clear

# quitter l'application
❯ quit
```

## Utiliser l'application en one shot

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

