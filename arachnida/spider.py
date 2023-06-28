import sys

def afficher_arguments():
    arguments = sys.argv[1:]  # Ignorer le premier argument (nom du script)
    for arg in arguments:
        print(arg)

afficher_arguments()
