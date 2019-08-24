import requests
from bs4 import BeautifulSoup


from .ETAPE_UNE import pole_emploi
def etape_UNE(lieu, emploi, rayon):
    """Dans un premier temps on cherche
    toutes les url de DESCRIPTION
    de pole qui match avec notre
    recherche,
    On aura donc la deuxieme partie du path"""

    print("ETAPE UNE")
    print("")

    liste_path = []

    liste_w1, lieu = pole_emploi(lieu, emploi, rayon)

    for i in liste_w1:
        liste_path.append(i)

    return liste_path



from .CONFIG import PATH_POLE_2
def ETAPE_DEUX(liste):
    """On cherche le path complet mtn en
    associant la premiere partie du path avec
    la seconde. Cela constitu la redirection vers la
    description du métier"""

    print("ETAPE DEUX")
    print("")

    recuperation_info = []

    compteur = 0
    array = 0
    liste_w = []
    for i in liste:
        if compteur == 20:
            recuperation_info.append(liste_w)
            liste_w = []
            compteur = 0
            
        path = PATH_POLE_2.format(i)
        liste_w.append(path)
        compteur += 1




    return recuperation_info



from .ETAPE_TROIS import verification_metier
def ETAPE_TROIS(liste, ville, LISTE_EMPLOI_UTILISATEUR):
    """We verify if the title is in adequation with
    our research"""

    print("ETAPE trois")
    print("")

    liste1 = []

 
    verification_metier_titre = verification_metier(liste, ville,
                                                    LISTE_EMPLOI_UTILISATEUR)

    if verification_metier_titre != []:
        liste1.append(verification_metier_titre)

    if liste1 == []:
        out = None
    else:
        out = liste1

    return out
         



from .ETAPE_QUATTRE import recherche_email
def ETAPE_QUATTRE(liste):
    """Maintenant on essais de chercher un
    email dans la recherche a gauche"""

    print("ETAPE quattre")
    print("")

    emails = []
    liste_no_mail = []

    for i in liste:
        email_trouvee = recherche_email(i)
        if email_trouvee != "":
            emails.append([email_trouvee, i])
        else:
            liste_no_mail.append(i)

    return emails, liste_no_mail



from .ETAPE_CINQ import recherche_entreprise_bas_de_page
def ETAPE_CINQ(liste_no_mail):

    print("ETAPE cinq")
    print("")

    liste = []
    liste_non_trouvee = []
    
    for i in liste_no_mail:
        entreprise_bas_page = recherche_entreprise_bas_de_page(i)

        if entreprise_bas_page != None:
            liste.append([entreprise_bas_page, i])
        else:
            liste_non_trouvee.append(i)

    return liste, liste_non_trouvee




from .ETAPE_SIX import identification_du_site
def ETAPE_SIX(liste):

    print(liste)

    print("ETAPE six")
    print("")
    liste1 = []
    for i in liste[0]:
        print(i)
        identification_site1 = identification_du_site(i[0])
        if identification_site1 != None:
            liste1.append([[identification_site1], i[0]])
            print(identification_site1)
        else:
            print("NANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")

                
    return liste1



from .ETAPE_SEPT import recherche_via_image
from .ETAPE_SEPT import recherche_CARRERBUILDER
from .ETAPE_SEPT import recherche_CARRERONLINE
from .ETAPE_SEPT import recherche_CARRERONLINE2
from .ETAPE_SEPT import recherche_CARRERONLINE3
from .ETAPE_SEPT import recherche_TALENTPLUG
from .ETAPE_SEPT import recherche_STEPSTONE
from .ETAPE_SEPT import recherche_MONSTER
from .ETAPE_SEPT import recherche_JOBCOLO
from .ETAPE_SEPT import recherche_INZEJOB
def ETAPE_SEPT(liste):


##
##    LISTE_EMPLOI_UTILISATEUR = [emploi]
##
##    lieu = lieu
##    rayon = "60"
##    liste_path = []
##
##
##    liste_url = etape_UNE(lieu, LISTE_EMPLOI_UTILISATEUR, rayon)
##    print(liste_url)
##    print("\n")
##
##
##    return liste_url
##
##    liste_description = ETAPE_DEUX(liste_url)
##    print(liste_description)
##    print("\n")
##    
##    #liste_description = [liste_description[0]]#a effacer
##    verification_metier_titre = ETAPE_TROIS(liste_description, lieu,
##                                            LISTE_EMPLOI_UTILISATEUR)
##
##    print(verification_metier_titre)
##    print("\n")
##    
##
##
##
##    emails, liste_no_mail = ETAPE_QUATTRE(verification_metier_titre)
##    print(emails)
##    print("\n")
##    print(liste_no_mail)
##
##
##
##    print("\n")
##    entreprise_bas_page, no_found = ETAPE_CINQ(liste_no_mail)
##    print(entreprise_bas_page)
##    print("")
##    print(no_found)
##    print("\n")
##
##
##
##
##    site = ETAPE_SIX(no_found)
##    print(site)



    print("\n")
    print("ETAPE SEPT")
    print("\n")
    ENTREPRISE = []
    for i in liste:
        print(i)
        
        url = recherche_via_image(i[1])
        print(url)

        if i[0][0].lower() == "careerbuilder":
            entreprise = recherche_CARRERBUILDER(url)
        
        elif i[0][0].lower() == "carriereonline":
            entreprise = recherche_CARRERONLINE(url)
            entreprise = recherche_CARRERONLINE2(entreprise, url)
            entreprise = recherche_CARRERONLINE3(entreprise, url)
        
        elif i[0][0].lower() == "talentplug":
            entreprise = recherche_TALENTPLUG(url)
        
        elif i[0][0].lower() == "stepstone":
            entreprise = recherche_STEPSTONE(url)

        elif i[0][0].lower() == "monster":
            entreprise = recherche_MONSTER(url)

        elif i[0][0].lower() == "joboolo":
            entreprise = recherche_JOBCOLO(url)

        elif i[0][0].lower() == "inzejob":
            entreprise = recherche_INZEJOB(url)

        try:
            #print(entreprise)
            ENTREPRISE.append([[entreprise], [url]])
        except:
            pass
        
    print("")



    print(ENTREPRISE)
    return ENTREPRISE




from .ETAPE_HUIT import recherche_google
from .ETAPE_HUIT import nettoyage_email
def ETAPE_HUIT(liste, lieu):

    print("ETAPE 8888888888888888")

    liste = recherche_google(liste, lieu)
    mail = nettoyage_email(liste)

    print(mail)
    return mail



    
    
