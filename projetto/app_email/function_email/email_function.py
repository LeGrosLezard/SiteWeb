import requests
from bs4 import BeautifulSoup

from site_scrap import pole_emploi


from site_scrap import recherche_via_image
from site_scrap import recherche_CARRERBUILDER
from site_scrap import recherche_CARRERONLINE
from site_scrap import recherche_CARRERONLINE2
from site_scrap import recherche_CARRERONLINE3
from site_scrap import recherche_TALENTPLUG
from site_scrap import recherche_STEPSTONE
from site_scrap import recherche_MONSTER
from site_scrap import recherche_JOBCOLO
from site_scrap import recherche_INZEJOB






def recherche_entreprise_via_google(nom, ville):
    pass



def etape_UNE(lieu, metier, rayon):
    """Dans un premier temps on cherche
    toutes les url de DESCRIPTION
    de pole qui match avec notre
    recherche,
    On aura donc la deuxieme partie du path"""
    
    for i in LISTE_EMPLOI_UTILISATEUR:
        liste_w1, lieu = pole_emploi(lieu, i, rayon)

        for i in liste_w1:
            liste_path.append(i)

    return liste_path







from CONFIG import PATH_POLE_2
def ETAPE_DEUX(liste):
    """On cherche le path complet mtn en
    associant la premiere partie du path avec
    la seconde. Cela constitu la redirection vers la
    description du métier"""

    recuperation_info = []

    for i in liste:
        path = PATH_POLE_2.format(i)
        recuperation_info.append(path)


    return recuperation_info



from site_scrap import verification_metier
def ETAPE_TROIS(liste, ville, LISTE_EMPLOI_UTILISATEUR):

    for i in liste:
        verification_metier_titre = verification_metier(liste, ville,
                                                        LISTE_EMPLOI_UTILISATEUR)


    return verification_metier_titre


from site_scrap import recherche_email
def ETAPE_QUATTRE(liste):
    """Maintenant on essais de chercher un
    email dans la recherche a gauche"""

    emails = []

    for i in liste:
        email_trouvee = recherche_email(i)
        if email_trouvee != "":
            emails.append(email_trouvee)

    if emails != []:
        out = emails
    else:
        out = None

    return out





if __name__ == "__main__":


    #def etape_mail():

    LISTE_EMPLOI_UTILISATEUR = ["python django"]

    lieu = "paris"
    rayon = "10"
    liste_path = []


    liste_url = etape_UNE(lieu, LISTE_EMPLOI_UTILISATEUR, rayon)
    #print(liste_url)
    liste_description = ETAPE_DEUX(liste_url)
    #print(liste_description)
    liste_description = [liste_description[0]]#a effacer
    verification_metier_titre = ETAPE_TROIS(liste_description, lieu,
                                            LISTE_EMPLOI_UTILISATEUR)
    #print(verification_metier_titre)

    email_trouvee = ETAPE_QUATTRE(verification_metier_titre)
    #print(email_trouvee)
    if email_trouvee == None:
        pass
        #c parti pour la recherche inter page
        #et on refait une fonction pour la pep
    else:
        pass
        #on cherche en bas de la page



    #def etape recherche








