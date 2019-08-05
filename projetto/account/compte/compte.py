import os
from .base_de_donnee.remplissage_user import insertion_user

from .CONFIG import PATH_FOLDER


def inscription(pseudo, nom, prenom, date, sexe, email,
                portable, fixe, adresse, password):
    
    insertion_user(nom, prenom, date, sexe, email,
                    fixe, password, pseudo, adresse,
                    portable)



def creation_dossier_user(pseudo):
    """Here we create a folder for user
    we input cv, motivation letter, message ..."""

    #os.chdir("/app/espace_user")
    nom_dossier = str(pseudo)
    print(PATH_FOLDER.format(nom_dossier))
    os.mkdir(PATH_FOLDER.format(nom_dossier))
