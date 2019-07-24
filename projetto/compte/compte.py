from .base_de_donnee.info_table import donnee_user
from .base_de_donnee.info_table import donnee_email
from .base_de_donnee.info_table import donnee_telephone_portable
from .base_de_donnee.info_table import insertion_user



def condition1(pseudo):
    """Vérification le pseudo n'existe pas deja"""

    out = ""
    
    verification_pseudo = donnee_user(pseudo)

    if verification_pseudo == pseudo:
        out = "Le pseudo existe déja. Vérifiez s'il vous plait" 

    else:
        out = ""


def condition2(email):
    """Verification l'email n'existe pas deja. Vérifiez s'il vous plait """

    out = ""

    verification_email = donnee_email(email)

    if verification_email == email:
        out = "L'email existe déja. Vérifiez s'il vous plait"

    else:
        out = ""


def condition3(portable):
    """Verification le portable n'existe pas deja"""

    out = ""

    verification_portable = donnee_telephone_portable(portable)

    if verification_portable == portable:
        out = "Le portable existe déja. Vérifiez s'il vous plait"

    else:
        out = ""





def inscription(pseudo, nom, prenom, date, sexe, email,
                portable, fixe, adresse, mot_de_passe):
    
    verif1 = condition1(pseudo)
    verif2 = condition2(email)
    verif3 = condition3(portable)

    liste = []

    if verif1 != "":
        liste.append(verif1)

    elif verif2 != "":
        liste.append(verif2)

    elif verif3 != "":
        liste.append(verif3)

    else:
        insertion_user(nom, prenom, prenom1, prenom2, prenom3,
                        date, sexe, email, fixe, password,
                        pseudo, lieu_habitation, portable)

    if liste == []:
        return "Enregistrement effectué avec Succes !"

    else:
        return liste





def connexion(password_connexion, pseudo_connexion):
    pass
















