import time
from rich.console import Console
from daily_tasks.task import TaskManager
from argparse import ArgumentParser, Namespace
from rich.align import Align
from rich.text import Text
from rich.rule import Rule
from rich.prompt import Prompt
from rich.panel import Panel
import shlex
import sys


console = Console()

# def main():

#     manager = TaskManager()

#     note = ArgumentParser(
#         description="CLI note taking app\n"
#         "  add <title>     : ajouter une note\n"
#         "  list            : lister les notes\n"
#         "  del <id>        : supprimer une note par son id\n"
#         "  done <id>       : marquer une note comme complétée\n"
#         "  display <id>    : afficher une note par son id"
#     )

#     # subcommands : add, list, del, done and display

#     subparsers = note.add_subparsers(dest = "command", help = "Commandes disponibles")
    
#     # add: note add 
#     add_parser = subparsers.add_parser("add", help = "Ajouter une note")
#     add_parser.add_argument("title", help = "Titre de la tache")

#     # list: note list
#     subparsers.add_parser("list", help = "Lister les notes")

#     # del: note del [id]
#     del_parser = subparsers.add_parser("del", help = "Supprimer une note par id")
#     del_parser.add_argument("id", type = int, help = "id de la note à supprimer")

#     # done: note done [id]

#     done_parser = subparsers.add_parser("done", help = "Marquer une tache comme completée")
#     done_parser.add_argument("id", type = int, help = "id de la note à marquer comme completée")

#     # display: note display [id]

#     display_parser = subparsers.add_parser("display", help = "Afficher une tache avec ses détails (id, titre, date et heure de création, statut de la tache (completée ou non)")
#     display_parser.add_argument("id", type = int, help = "id de la tache à afficher")


#     argments = note.parse_args()

#     # dispatch
#     if argments.command == "add":
#         manager.add_task(argments.title)
#     elif argments.command == "list":
#         manager.list_tasks()
#     elif argments.command == "del":
#         manager.delete_task(argments.id)
#     elif argments.command == "display":
#         manager.display_task(argments.id)
#     elif argments.command == "done":
#         manager.mark_task_as_completed(argments.id)



banner = r"""
   _____ _      _____   _   _  ____ _______ ______ _____ 
  / ____| |    |_   _| | \ | |/ __ \__   __|  ____|  __ \
 | |    | |      | |   |  \| | |  | | | |  | |__  | |__) |
 | |    | |      | |   | . ` | |  | | | |  |  __| |  _  /
 | |____| |____ _| |_  | |\  | |__| | | |  | |____| | \ \
  \_____|______|_____| |_| \_|\____/  |_|  |______|_|  \_\
"""

def show_banner():
    console.print()
    console.print(Align.center(Text(banner, style = "bold cyan")))
    console.print(Rule(Text("✦ Daily Tasks CLI ✦", style="bold magenta")))
    console.print(
         Align.center(
              Text("Tapez help pour la liste des commandes • 'quit' pour quitter", style = "italic yellow")
         )
    )
    console.print()


def show_help():
    console.print(Panel.fit(
        Text.from_markup(
            "[bold green]help[/]            afficher cette aide\n"
            "[bold green]add <title>[/]    ajouter une tâche\n"
            "[bold green]list[/]           lister les tâches\n"
            "[bold green]del <id>[/]       supprimer une tâche\n"
            "[bold green]done <id>[/]      marquer une tâche comme complétée\n"
            "[bold green]display <id>[/]   afficher une tâche par son id\n"
            "[bold green]clear[/]          effacer l'écran\n"
            "[bold green]quit / exit[/]    quitter l'application"
        ),
        title="[bold blue]Commandes[/]",
        border_style="bold blue",
    ))

def dispatch(manager, command, args):
    """Retourne False pour quitter la boucle, True sinon."""
    if command == "help":
        show_help()

    elif command == "add":
        if not args:
            console.print("[red]Erreur : titre manquant. Usage : add <title>[/]")
            return True
        manager.add_task(" ".join(args))

    elif command == "list":
        manager.list_tasks()

    elif command == "del":
        if not args:
            console.print("[red]Erreur : id manquant. Usage : del <id>[/]")
            return True
        try:
            manager.delete_task(int(args[0]))
        except ValueError:
            console.print(f"[red]'{args[0]}' n'est pas un entier valide.[/]")

    elif command == "done":
        if not args:
            console.print("[red]Erreur : id manquant. Usage : done <id>[/]")
            return True
        try:
            manager.mark_task_as_completed(int(args[0]))
        except ValueError:
            console.print(f"[red]'{args[0]}' n'est pas un entier valide.[/]")

    elif command == "display":
        if not args:
            console.print("[red]Erreur : id manquant. Usage : display <id>[/]")
            return True
        try:
            manager.display_task(int(args[0]))
        except ValueError:
            console.print(f"[red]'{args[0]}' n'est pas un entier valide.[/]")

    elif command == "clear":
        console.clear()

    elif command in ("quit", "exit", "q"):
        console.print("[yellow] Leaving the app ... [/]")
        return False

    else:
        console.print(
            f"[red]Commande inconnue : '{command}'. "
            f"Tape 'help' pour la liste des commandes.[/]"
        )
    return True

def interactive_loop(manager):
    show_banner()
    running = True
    while running:
        try:
            user_input = Prompt.ask("[bold magenta]daily-tasks[/] ❯").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[yellow]Leaving the app ...[/]")
            break

        if not user_input:
            continue  # ligne vide -> on ne fait rien

        try:
            parts = shlex.split(user_input)
        except ValueError as e:
            console.print(f"[red]Erreur de syntaxe : {e}[/]")
            continue

        running = dispatch(manager, parts[0], parts[1:])


def run_one_shot(manager):
    """Mode CLI classique quand des arguments sont passés depuis le shell."""
    note = ArgumentParser(
        description="CLI note taking app\n"
        "  add <title>     : ajouter une note\n"
        "  list            : lister les notes\n"
        "  del <id>        : supprimer une note par son id\n"
        "  done <id>       : marquer une note comme complétée\n"
        "  display <id>    : afficher une note par son id"
    )
    subparsers = note.add_subparsers(dest="command", help="Commandes disponibles")

    add_parser = subparsers.add_parser("add", help="Ajouter une note")
    add_parser.add_argument("title", help="Titre de la tache")

    subparsers.add_parser("list", help="Lister les notes")

    del_parser = subparsers.add_parser("del", help="Supprimer une note par id")
    del_parser.add_argument("id", type=int, help="id de la note à supprimer")

    done_parser = subparsers.add_parser("done", help="Marquer une tache comme completée")
    done_parser.add_argument("id", type=int, help="id de la note à marquer comme completée")

    display_parser = subparsers.add_parser("display", help="Afficher une tache avec ses détails")
    display_parser.add_argument("id", type=int, help="id de la tache à afficher")

    args = note.parse_args()

    if args.command == "add":
        manager.add_task(args.title)
    elif args.command == "list":
        manager.list_tasks()
    elif args.command == "del":
        manager.delete_task(args.id)
    elif args.command == "display":
        manager.display_task(args.id)
    elif args.command == "done":
        manager.mark_task_as_completed(args.id)
    elif args.command is None:
        note.print_help()


def main():
    manager = TaskManager()
    # Sans argument → mode interactif (REPL)
    # Avec argument(s) → mode one-shot (argparse)
    if len(sys.argv) > 1:
        run_one_shot(manager)
    else:
        interactive_loop(manager)

if __name__ == '__main__':
        main()