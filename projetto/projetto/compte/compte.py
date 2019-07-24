from .base_de_donnee.info_table import donnee_user
from .base_de_donnee.info_table import donnee_email
from .base_de_donnee.info_table import donnee_telephone_portable
from .base_de_donnee.remplissage_user import insertion_user



def condition1(pseudo):
    """Vérification le pseudo n'existe pas deja"""

    out = ""
    
    verification_pseudo = donnee_user(pseudo)

    if verification_pseudo == pseudo:
        out = "Le pseudo existe déja. Vérifiez s'il vous plait" 

    else:
        out = ""

    return out


def condition2(email):
    """Verification l'email n'existe pas deja. Vérifiez s'il vous plait """

    out = ""

    verification_email = donnee_email(email)

    if verification_email == email:
        out = "L'email existe déja. Vérifiez s'il vous plait"

    else:
        out = ""

    return out



def condition3(portable):
    """Verification le portable n'existe pas deja"""

    out = ""

    verification_portable = donnee_telephone_portable(portable)

    if verification_portable == portable:
        out = "Le portable existe déja. Vérifiez s'il vous plait"

    else:
        out = ""

    return out




def inscription(pseudo, nom, prenom, date, sexe, email,
                portable, fixe, adresse, password):
    
    verif1 = condition1(pseudo)
    verif2 = condition2(email)
    verif3 = condition3(portable)

    liste = []

    if verif1 != "":
        liste.append(verif1)

    if verif2 != "":
        liste.append(verif2)

    if verif3 != "":
        liste.append(verif3)

    
    if verif1 == "" and verif2 == "" and verif3 == "":

        insertion_user(nom, prenom, date, sexe, email,
                       fixe, password, pseudo, adresse,
                       portable)

        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)




    if liste == []:
        return "Enregistrement effectué avec Succes !"

    else:
        return liste




from .base_de_donnee.connexion import verifier_connexion
from .base_de_donnee.connexion import connexion_database
def connexion(password_connexion, pseudo_connexion):
    
    pseudo, password = verifier_connexion(pseudo_connexion, password_connexion)
    connexion_database(pseudo, password)



def deconnexion(pseudo, password):
    pass













