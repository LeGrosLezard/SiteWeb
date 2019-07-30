import requests
from bs4 import BeautifulSoup




from CONFIG import PATH_POSTAL
def function_code_postal(lieu):
    """Here we recup the postal code of the current place."""

    path = PATH_POSTAL.format(lieu)
    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.find_all("h2")

    liste = []
    liste.append(propriete)

    return liste



def code_postal(lieu):
    """Thank to the postal code we can
    call the URL of weather. Indeed,
    this url need the city and the postal code."""

    liste = function_code_postal(lieu)

    code = ''
    liste_code = []

    for i in liste[0]:
        for j in i:
            for k in j:
                try:
                    k = int(k)
                    if k == int(k):
                        code += str(k)

                except ValueError:
                    if code != '':
                        liste_code.append(code)
                        code = ''
                    else:
                        pass


    return liste_code[0]







from CONFIG import PATH_POLE
def pole_emploi(lieu, emploi, rayon):

    code = code_postal(lieu)


    path = PATH_POLE.format(code, emploi, rayon)
    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")

    
    propriete = soup_html.findAll("div",{"class":"media"})

    liste_w1 = []
    
    for i in propriete:
        #Pour chaque élément trouvé cad chaque annonce,
        #on cherche la suite(le détail de l'annonce)
        #qui se traduit par href.......
        
        liste_w = []
        liste_w.append(str(i.a))
        #On récupere tous les href
        
        url = ""
        
        for i in liste_w:
            
            c = 0
            ok = False

            
            for j in i:
                #Pour chaque element de la div
                
                if i[c] == "h" and i[c + 1] == "r" and i[c + 2] == "e"\
                   and i[c + 3] == "f":
                    ok = True
                    c += 3
                    #On cherche le mot href
                    #si on le trouve on dit ok = True
                    #qui permet la mise en liste et on ajout + 3
                    #au counter (qui premet de nous balader dans un element)
                
                if ok is True:
                    if j == " ":
                        pass
                    #Si j est un espace vide on l'ignore
                    #comme ca on a pas l'espace dans notre url
                    else:
                        url += j
                        #Sinon on ajoute j a notre url
                
                else:
                    c += 1
                    #Si rien ne se produit, on increment la variable

                if ok is True and j == " ":
                    liste_w1.append(url[6:-1])
                    break
                #Si j est un espace (que l'on a ingoré dans notre incrémentaiton)
                #On arrete tout, on
                #ajoute a notre liste que l'on retourne l'url
                #de 6 a -1 car on ignore les guillement de fin et
                #le href du début (bie nque l'on est mis c + 3)
                


    return liste_w1, lieu

    #ICI IL FAUT ABSOLUMENT FAIRE UN RETOUR AJAX PUIS
    #~RENVOYER UN AUTRE CALL




def titre(path):
    """On récupere le titre"""
    
    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.findAll("h1",{"class":"t2 title"})

    liste = []
    for i in propriete:
        liste.append(str(i.string.lower()))
        
    return liste
    


LISTE_EMPLOI_UTILISATEUR = ["developpeur", "développeur python",
                            "développeur backend",
                            "déveleppeur application web python",
                            "python django"]

from CONFIG import PATH_POLE_2
def verification_metier(liste, ville):
    """Ici on va voir si le titre == la recherche emploie
    de l'utilisateur

    On va aussi essayer de récupérer l'entreprise qui
    veut recruter.
    """
    
    
    global LISTE_EMPLOI_UTILISATEUR

    liste_sauvegarde = []

    for i in liste:

        path = PATH_POLE_2.format(i)
        recuperation1 = titre(path)

        for emploi in LISTE_EMPLOI_UTILISATEUR:
            finding_emploi = str(recuperation1).find(str(emploi.strip()))
            if finding_emploi >= 0:
                liste_sauvegarde.append([recuperation1, [i]])
    


    #print(liste_sauvegarde)
    return liste_sauvegarde




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
        return liste_alpha_numeric1, "adresse trouvée"
    else:
        return "", ""



def recherche_via_image(path):
    
    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.findAll("div",{"class":"modal-apply"})

    liste_propriete = []
    liste_propriete.append(str(propriete))

    c = 0
    ok = False
    url = ""
    liste_final = []
    
    for i in liste_propriete:
        
        for j in i:
            if i[c] == "h" and\
               i[c + 1] == "r" and\
               i[c + 2] == "e" and\
               i[c + 3] == "f":
                ok = True

            if ok is True:
                url += i[c]

            if i[c] == " ":
                liste_final.append(url)
                url = ""
                ok = False
            c += 1


    liste_final_return = []
    for i in liste_final:
        if i != "":
            liste_final_return.append(i[6:-2])


    return liste_final_return




def recherche_appuie_image(path):
    """On cherche qui a posté cette anonce"""

    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.findAll("div",{"class":"bloc clear nm col-2 small-marge"})

    liste_propriete = []
    liste_propriete.append(str(propriete))


    c = 0
    entrprise = ""
    ok = False
    liste = []
    for i in liste_propriete:
 
        for j in i:
            if i[c] == "p" and\
               i[c + 1] == "o" and\
               i[c + 2] == "s" and\
               i[c + 3] == "t" and\
               i[c + 4] == "é" and\
               i[c + 5] == " " and\
               i[c + 6] == "p" and\
               i[c + 7] == "a" and\
               i[c + 8] == "r" and\
               i[c + 9] == " ":
                ok = True

            if ok is True:
                entrprise += i[c]
                
            if i[c] == "<":
                ok = False
                liste.append(entrprise)

            c += 1

    return entrprise[10:-1]

def recherche_entreprise_via_google(nom, ville):
    pass

def recherche_email_dans_description(path):
    pass
    
def recherche_entreprise(liste):
    """On cherche l'entreprise mtn"""

    recuperation_info = []
    
    for i in liste:

        #FAUT PRECISER LE NUMERO DE LOFFRE

        path = PATH_POLE_2.format(i[1][0])

        
        email, trouvee = recherche_email(path)
        #onglet info on cherche email

        if trouvee == "adresse trouvée":
            pass
        
        else:
            recherche_par_image = recherche_via_image(path)
            entreprise = recherche_appuie_image(recherche_par_image[0])
            #si ya pas demail ya la société qui demande
            #on click sur le href et on cherche la société











##for i in LISTE_EMPLOI_UTILISATEUR:
##    liste, ville = pole_emploi("paris", i, "20")
##    verification_metier_plus_details(liste, ville)

#VA PRENDRE PLEIN DE TEMPS CA....
    
#liste, ville = pole_emploi("paris", "développeur python django", "20")

liste = [[['développeur python/django h/f'],
         ['/offres/recherche/detail/9211622']],]


liste1 = recherche_entreprise(liste)






