from daily_tasks.task import TaskManager
from argparse import ArgumentParser, Namespace




def main():

    manager = TaskManager()

    note = ArgumentParser(
        description="CLI note taking app\n"
        "  add <title>     : ajouter une note\n"
        "  list            : lister les notes\n"
        "  del <id>        : supprimer une note par son id\n"
        "  done <id>       : marquer une note comme complétée\n"
        "  display <id>    : afficher une note par son id"
    )

    # subcommands : add, list, del, done and display

    subparsers = note.add_subparsers(dest = "command", help = "Commandes disponibles")
    
    # add: note add 
    add_parser = subparsers.add_parser("add", help = "Ajouter une note")
    add_parser.add_argument("title", help = "Titre de la tache")

    # list: note list
    subparsers.add_parser("list", help = "Lister les notes")

    # del: note del [id]
    del_parser = subparsers.add_parser("del", help = "Supprimer une note par id")
    del_parser.add_argument("id", type = int, help = "id de la note à supprimer")

    # done: note done [id]

    done_parser = subparsers.add_parser("done", help = "Marquer une tache comme completée")
    done_parser.add_argument("id", type = int, help = "id de la note à marquer comme completée")

    # display: note display [id]

    display_parser = subparsers.add_parser("display", help = "Afficher une tache avec ses détails (id, titre, date et heure de création, statut de la tache (completée ou non)")
    display_parser.add_argument("id", type = int, help = "id de la tache à afficher")


    argments = note.parse_args()

    # dispatch
    if argments.command == "add":
        manager.add_task(argments.title)
    elif argments.command == "list":
        manager.list_tasks()
    elif argments.command == "del":
        manager.delete_task(argments.id)
    elif argments.command == "display":
        manager.display_task(argments.id)
    elif argments.command == "done":
        manager.mark_task_as_completed(argments.id)

if __name__ == '__main__':
        main()