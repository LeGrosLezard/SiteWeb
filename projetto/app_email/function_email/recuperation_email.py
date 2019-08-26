import requests
from bs4 import BeautifulSoup



from site_scrap import pole_emploi
def etape_UNE(lieu, emploi, rayon):
    """Dans un premier temps on cherche
    toutes les url de DESCRIPTION
    de pole qui match avec notre
    recherche,
    On aura donc la deuxieme partie du path"""

    print("ETAPE UNE")
    print("")

    liste_path = []

    liste_w1, lieu = pole_emploi(lieu, emploi, "60")
    for i in liste_w1:
        liste_path.append(i)

    print(liste_path)
    return liste_path




from CONFIG import PATH_POLE_2
def ETAPE_DEUX(liste):
    """On cherche le path complet mtn en
    associant la premiere partie du path avec
    la seconde. Cela constitu la redirection vers la
    description du métier"""

    print("ETAPE DEUX")
    print("")

    recuperation_info = []

    for i in liste:
        path = PATH_POLE_2.format(i)
        recuperation_info.append(path)

    print(recuperation_info)
    return recuperation_info




from site_scrap import verification_metier
def ETAPE_TROIS(liste, ville, LISTE_EMPLOI_UTILISATEUR):
    """On verifie le titre de l'offre et la recherche de la
    personne pour etre sur de postuler au bon endroit"""

    print("ETAPE trois")
    print("")

    liste1 = []

    for i in liste:
        print(i)
        verification_metier_titre = verification_metier(i, ville,
                                                        LISTE_EMPLOI_UTILISATEUR)

        if verification_metier_titre != []:
            liste1.append(verification_metier_titre)

    if liste1 == []:
        out = None
    else:
        out = liste1
        
    print(out)
    return out
         

    
from site_scrap import recherche_email
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



from site_scrap import recherche_entreprise_bas_de_page
def ETAPE_CINQ(liste_no_mail):
    """Nous n'avons pas trouvé demail pour ces demandes
    nous recherchons alors le nom de l'entreprise en bas de page
    (ibnformation donnée par pole emploi)
    pour rechercher ensuite son email"""

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



from site_scrap import identification_du_site
def ETAPE_SIX(liste):
    """Nous n'avons pas trouvé d'entreprise
    pour la recherche d'email.
    Donc nous allons sur le site partenaire
    chercher le nom de l'entreprise. Pour cela
    nous prenons le nom du site partenaire
    et pour chaque site on cherche le nom
    de l'entreprise demandeur
    """

    print("ETAPE six")
    print("")


    liste1 = []
    for i in liste:
        try:
            identification_site = identification_du_site(i)
            if identification_site != None:
                liste1.append([[identification_site], i])
        except:
            identification_site = identification_du_site(i[0])
            if identification_site != None:
                liste1.append([[identification_site], i[0]])

                
    return liste1




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
from site_scrap import recherche_google

def ETAPE_SEPT(liste):

    print("ETAPE SEPT")
    print("")


    entreprise = ""
    url = ""

    liste_ok = []
    
    for i in liste:
        print(i)
        
        url = recherche_via_image(i[1])


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

        if entreprise == "":
            pass
        else:
            liste_ok.append([entreprise, url])
        
    return liste_ok




def ETAPE_HUIT(liste_email):
    print("ETAPE HUIT")
    print("")

    liste = []
    for i in liste_email:
        for j in i:
            liste.append([j[0], j[1][0]])

    mail = []
    for i in liste:

        m = recherche_google(i[0], "valence")
        mail.append([m, i[1]])

    return mail



from site_scrap import liste_1
from site_scrap import liste_2
def ETAPE_NEUF(liste_a, liste_b):
    mail1 = liste_1(liste_a)
    mail2 = liste_2(liste_b)

    return mail1, mail2



from database.database import mail_verification
from database.database import mail_stock
def data(pseudo):
    
    liste = mail_verification

    #AFAIRE

    
    for i in mail1: 
        mail_stock(pseudo, i[0], i[1], "")

    for i in mail2:
        mail_stock(pseudo, i[0], i[1], "")
    
    

if __name__ == "__main__":

    EMAIL = []
    ENTREPRISE = []
    
    rayon = "60"
    lieu = "valence"
    emploi = "Développeur web python"
    pseudo = ""

    liste = etape_UNE(lieu, emploi, rayon)
    liste = ETAPE_DEUX(liste)
    liste = ETAPE_TROIS(liste, lieu, emploi)
    email, liste = ETAPE_QUATTRE(liste)
    EMAIL.append(email)

    entreprise, liste = ETAPE_CINQ(liste)
    ENTREPRISE.append(entreprise)

    liste = ETAPE_SIX(liste)
    liste = ETAPE_SEPT(liste)

    ENTREPRISE.append(liste)

    final = ETAPE_HUIT(ENTREPRISE)

    mail1, mail2 = ETAPE_NEUF(final, EMAIL)
    print(mail1, mail2)






























