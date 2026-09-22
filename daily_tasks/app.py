from daily_tasks.task import TaskManager
from argparse import ArgumentParser, Namespace


manager = TaskManager()

manager.list_tasks()

def main():

    parser = ArgumentParser()

    parser.add_argument('add', help = "Ajouter un tache")

    # add a task
    parser.add_argument('list', help = "Lister les taches")

    # list tasks
    parser.add_argument('list', help = "Lister les taches")

    # delete a task
    parser.add_argument('del', help = "Supprimer une tache \n Vous fournisser l'id de la tache : \n>del 2 --> supprime la tache d'id 2")

    # mark as completed
    parser.add_argument('done', help = "Marquer une tache une tache comme complétée \n Vous fournisser l'id de la tache : \n>done 2 --> marque la tache d'id 2 comme complétée")

    # afficher une tache spécifique
    parser.add_argument('display', help = "Afficher une tache \n Vous fournisser l'id de la tache : \n>display 2 --> affiche la tache d'id 2 ")

    args = parser.parse_args()

    if __name__ == '__main__':
        main()