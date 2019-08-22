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





def etape_UNE(lieu, LISTE_EMPLOI_UTILISATEUR, rayon):
    """Dans un premier temps on cherche
    toutes les url de DESCRIPTION
    de pole qui match avec notre
    recherche,
    On aura donc la deuxieme partie du path"""

    print("ETAPE UNE")
    print("")

    liste_path = []
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

    print("ETAPE DEUX")
    print("")

    recuperation_info = []

    for i in liste:
        path = PATH_POLE_2.format(i)
        recuperation_info.append(path)


    return recuperation_info






from site_scrap import verification_metier
def ETAPE_TROIS(liste, ville, LISTE_EMPLOI_UTILISATEUR):

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
         
    #return verification_metier_titre


from site_scrap import recherche_email
def ETAPE_QUATTRE(liste):
    """Maintenant on essais de chercher un
    email dans la recherche a gauche"""


    print("ETAPE quattre")
    print("")

    emails = []
    liste_no_mail = []
    

    for i in liste:
        print(i)
        email_trouvee = recherche_email(i)
        if email_trouvee != "":
            emails.append([email_trouvee, i])
        else:
            liste_no_mail.append(i)

    return emails, liste_no_mail



from site_scrap import recherche_entreprise_bas_de_page
def ETAPE_CINQ(liste_no_mail):

    print("ETAPE cinq")
    print("")

    liste = []
    liste_non_trouvee = []
    for i in liste_no_mail:
        print(i)
        entreprise_bas_page = recherche_entreprise_bas_de_page(i)

        if entreprise_bas_page != None:
            liste.append([entreprise_bas_page, i])
        else:
            liste_non_trouvee.append(i)

    return liste, liste_non_trouvee




from site_scrap import identification_du_site
def ETAPE_SIX(liste):

    print("ETAPE six")
    print("")


    liste1 = []
    for i in liste:
        print(i)
        try:
            identification_site = identification_du_site(i)
            print(identification_site)
            if identification_site != None:
                liste1.append([[identification_site], i])
        except:
            identification_site = identification_du_site(i[0])
            print(identification_site)
            if identification_site != None:
                liste1.append([[identification_site], i[0]])

                
    return liste1





def recherche_email_final(emploi, lieu, rayon):


    #def etape_mail():

    

    LISTE_EMPLOI_UTILISATEUR = [emploi]

    lieu = lieu
    rayon = rayon
    liste_path = []


    liste_url = etape_UNE(lieu, LISTE_EMPLOI_UTILISATEUR, rayon)
    print(liste_url)
    print("\n")

    liste_description = ETAPE_DEUX(liste_url)
    print(liste_description)
    print("\n")
    
    #liste_description = [liste_description[0]]#a effacer
    verification_metier_titre = ETAPE_TROIS(liste_description, lieu,
                                            LISTE_EMPLOI_UTILISATEUR)

    print(verification_metier_titre)
    print("\n")
    



    emails, liste_no_mail = ETAPE_QUATTRE(verification_metier_titre)
    print(emails)
    print("\n")
    print(liste_no_mail)



    print("\n")
    entreprise_bas_page, no_found = ETAPE_CINQ(liste_no_mail)
    print(entreprise_bas_page)
    print("")
    print(no_found)
    print("\n")




    site = ETAPE_SIX(no_found)
    print(site)

    print("\n")
    print("ETAPE SEPT")
    print("\n")
    
    for i in site:
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
    print(emails)
    #print(entreprise_bas_page)
    #print(ENTREPRISE)

    #print(lieu)






if __name__ == "__main__":
    recherche_email_final("menuisier", "lyon", "60")












    
    
