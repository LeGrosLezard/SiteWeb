import requests
from bs4 import BeautifulSoup

def recherche_email(path):
    """Sur le site y'a un un dispositif a l'information
    a gauche, on cherche si ya l'adresse email dans cet onglet"""


    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.findAll("div",{"class":"modal-apply"})

    liste_alpha_numeric = []
    liste_alpha_numeric1 = []

    for i in str(propriete):
        email = str(i).find("@")
        #On cherche dans la description si y'a une addresse mail
        #par le @
        
        addresse_mail = ""
        ok = False
        #On initialise deux variable
        #laddresse mail qui nous sert d'incrementation
        #ok qui dira a la boucle si on doit incrementer ou pas
        
        if email >= 0:
            #Donc si on trouve un mail
            
            for i in str(propriete):
                for j in i:
                    #On parcourt les balise
     
                    if j == ">":
                        ok = True
                        #Dans un premier temps si on trouve une
                        #balise fermant
                        #on dit ok is True
                        #Commence l'incrementation


                    if j == "<":
                        liste_alpha_numeric.append(addresse_mail)
                        addresse_mail = ""
                        ok = False
                        #Si on trouve un balise ouvrant
                        #On ajout la variable incrémenté
                        #a notre liste
                        #on dit ok est false
                        #stop incrémentation
                        #on vide la balise

                    if ok is True:
                        addresse_mail += j
                        #si ok est vrai alors on incrémente la balise


    for i in liste_alpha_numeric:
        find = str(i).find(str("@"))
        if find >= 0:
            if i[:2] == ">\n":
                liste_alpha_numeric1.append(i[2:])
            else:
                liste_alpha_numeric1.append(i)
            #Dans notre liste d'incrémentation
            #on trouve l'addresse mail
            #et on efface le retour de ligne
                

    if liste_alpha_numeric1 != []:
        return liste_alpha_numeric1
    else:
        return ""

