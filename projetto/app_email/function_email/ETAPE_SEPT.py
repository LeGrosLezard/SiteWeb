import requests
from bs4 import BeautifulSoup


def recherche_via_image(path):
    """Ici c'est comme si on appuyait sur
    l'image dans la description"""

    
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

    try:
        return liste_final_return
    except IndexError:
        return None








def recherche_CARRERBUILDER(path):
    """On cherche qui a posté cette anonce"""
    #CARRERBUILDER
    
    request_html = requests.get(path[0])
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
    try:
        return entrprise[10:-1]
    except IndexError:
        return None







def recherche_CARRERONLINE(path):
    """On cherche qui a posté cette anonce"""
    #CARRERONLINE
    
    request_html = requests.get(path[0])
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.findAll("div",{"class":"dann2015_infosrecruteur"})

    liste_propriete = []
    liste_propriete.append(str(propriete))

    liste_propriete1 = []
    c = 0
    ok = False
    entreprise = ""
    for i in liste_propriete:
        for j in i:
            if i[c] == "R" and\
               i[c + 1] == "e" and\
               i[c + 2] == "c" and\
               i[c + 3] == "r" and\
               i[c + 4] == "u" and\
               i[c + 5] == "t" and\
               i[c + 6] == "e" and\
               i[c + 7] == "u" and\
               i[c + 8] == "r" and\
               i[c + 9] == " " and\
               i[c + 10] == ":" and\
               i[c + 11] == " ":
                ok = True
                
            if ok is True:
                entreprise += i[c]

            if i[c] == "/":
                ok = False
                liste_propriete1.append(entreprise)
                entreprise = ""
                
            c += 1

    liste_propriete2 = []

    for i in liste_propriete1:
        if i == '':
            pass
        else:
            liste_propriete2.append(i)

    try:
        return liste_propriete2[0][20:-2]
    except IndexError:
        return None


def recherche_CARRERONLINE2(liste, path):
    """Si l'entreprise n'y est pas alors on
    essais d'aller sur le site web demandeur"""
    if liste == []:
        
        request_html = requests.get(path[0])
        page = request_html.content
        soup_html = BeautifulSoup(page, "html.parser")
        propriete = soup_html.findAll("div",{"class":"det_col"})
        
        liste_propriete = []
        liste_propriete1 = []

        for i in propriete:
            liste_propriete.append(str(i.a))

     
        c = 0
        ok = False
        entreprise = ""
        liste_propriete1 = []
        for i in liste_propriete:
            for j in i:
                if i[c] == "h" and\
                   i[c + 1] == "r" and\
                   i[c + 2] == "e" and\
                   i[c + 3] == "f":
                    ok = True

                if ok is True:
                    entreprise += i[c]

                if i[c] == " ":
                    ok = False
                    liste_propriete1.append(entreprise)
                    entreprise = ""
                    
                c += 1

        liste_propriete2 = []
        for i in liste_propriete1:
            if i == '':
                pass
            else:
                liste_propriete2.append(i)

        out =  liste_propriete2[0][6:-2]
        out = recherche_CARRERONLINE3(out)


        
    else:
        out = liste

    return out


def recherche_CARRERONLINE3(liste, path):
    request_html = requests.get(path[0])
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.find("div",{"class":"coord_txt"})

    out = str(propriete)

    return out
#erreur si y'a rien mais nik




def recherche_TALENTPLUG(path):
    """On cherche qui a posté cette anonce"""
    #TALENTPLUG
    
    request_html = requests.get(path[0])
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.findAll("h3")

    liste_propriete = []

    for i in propriete:
        liste_propriete.append(str(i.get_text()))


    entreprise = []
    for i in liste_propriete:
        find = str(i).find("A propos de ")
        if find >= 0:
            entreprise.append(i)
    try:
        return str(entreprise[0][12:-2])
    except IndexError:
        return None


def recherche_STEPSTONE(path):
    """On cherche qui a posté cette anonce"""
    #STEPSTONE
    
    request_html = requests.get(path[0])
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.findAll("h6")

    liste = []
    for i in propriete:
        liste.append(i.get_text())

    try:
        return liste[0][1:-1]
    except IndexError:
        return None


def recherche_MONSTER(path):
    """On cherche qui a posté cette anonce"""
    #MONSTER
    
    request_html = requests.get(path[0])
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.findAll("h1")

    
    liste = []
    liste1 = [[],[],[]]

    c = 0
    for i in propriete:
        liste.append(str(i.get_text()))
        
    for i in liste:

        part = ""
        
        for j in i:
            if j == "-":
                liste1[c].append(part)
                c += 1
                part = ""
            else:
                part += j

    
    liste1[c].append(part)
    try:
        return liste1[2][0]
    except IndexError:
        return None

    
    #if info recruteur
    #else:
    #click image




def recherche_JOBCOLO(path):
    """On cherche qui a posté cette anonce"""
    #JOBOOLO
    #des fois y'a pas l'entreprise faut du coup scrapper le text
    #sinon laisse tomber

    request_html = requests.get(path[0])
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.findAll("div",{"annonce_item"})

    liste = []
    c = 0
    ok = False
    for i in propriete:
        liste.append(str(i.get_text()))

    liste1 = []
    for i in liste:
        nom = ""
        
        for j in i:
            try:
                if i[c] == "S" and\
                   i[c + 1] == "o" and\
                   i[c + 2] == "c" and\
                   i[c + 3] == "i" and\
                   i[c + 4] == "é" and\
                   i[c + 5] == "t" and\
                   i[c + 6] == "é" and\
                   i[c + 7] == " " and\
                   i[c + 8] == ":" and\
                   i[c + 9] == " ":
                    ok = True
                    
                if ok is True: 
                    nom += j

                if i[c] == " " and i[c + 1] == "-" and\
                   i[c + 2] == " ":
                    ok = False
                    liste1.append(nom)
                    nom = ""
                c += 1
                
            except IndexError:
                pass
  
    liste2 = []
    for i in liste1:
        if i == "":
            pass
        else:
            liste2.append(i)
    try:
        return liste2[0][10:-2]
    except IndexError:
        return None
    #if info recruteur
    #else:
    #click image



def recherche_INZEJOB(path):
    """On cherche qui a posté cette anonce"""
    #INZEJOB
    #des fois y'a pas l'entreprise faut du coup scrapper le text
    #sinon laisse tomber
    
    request_html = requests.get(path[0])
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.find_all("span", {"class":"info"})


 


    liste = [[],[],[],[]]
    
    c = 0
    for i in propriete:
        liste[c].append(str(i.get_text()))
        c+=1

    for i in liste:
        if i == []:
            out = None
        else:
            return liste[2][0]


def recherche_1TAF_COM(path):
    """On cherche qui a posté cette anonce"""
    #1TAF.COM
    #la faut chopper l'url qu'ils donne et ensuite
    #aller dessus récuper le truk qui demande
    
    request_html = requests.get(path[0])
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.findAll("blockquote",{"id":"conditions-part"})

    liste = []
    liste.append(str(propriete))

    url = ""
    c = 0
    ok = False
    liste1 = []
    for i in liste:
        for j in i:

            if i[c] == "h" and\
               i[c + 1] == "t" and\
               i[c + 2] == "t" and\
               i[c + 3] == "p":
                ok = True
                
            if ok is True:
                url += i[c]
                
            if i[c] == " ":
                ok = False
                liste1.append(url)
                url = ""
                
                
            c += 1

    liste2 = []

    for i in liste1:
        if i == "":
            pass
        else:
            liste2.append(i)

    try:
        return liste2[0][:-2]
    except IndexError:
        return None

def recherche_1TAF_COM1(path):
    pass


#---------------------------------------------------Traitement liste

def traitement(liste1, liste2):
    liste_traitee = []

    for i in liste1:

        finding = str(i[0]).find("\n")
        if finding >= 0:
            liste_traitee.append([i[0][1:-1], i[1][0]])
        else:
            liste_traitee.append([i[0], i[1][0]])



    for i in liste2:

        if i[0][0] == None:
            pass
        else:
            liste_traitee.append([i[0][0], i[1][0][0]])

    return liste_traitee


#----------------------------------------------------GOOGLE RECHERCHE
from .CONFIG import PATH_GOOGLE
def recherche_google(liste, lieu):

    final = []
    #i[1] c'est la page de référence de pole emploie
    for element in liste:
        recherche = element[0].replace(" ", "+")
        print(element)
        path = PATH_GOOGLE.format(recherche, lieu)
        request_html = requests.get(path)
        page = request_html.content
        soup_html = BeautifulSoup(page, "html.parser")
        propriete = soup_html.find_all("div")

        liste_div = []
        email = []
        for i in propriete:

            liste_div.append(str(i.get_text()))
            
            for i in liste_div:

                adresse = ""
                
                for j in i:

                    if j == " ":

                        arobase = str(adresse).find("@")
                        if arobase >= 0:
                            email.append(adresse)
                        adresse = ""
                    
                    adresse += j

            

        print(set(email))
        final.append([set(email), element])
    

    for i in final:
        print(i)


    return final



def nettoyage_email(liste):

    liste_none = []
    liste_traitement = []
    for i in liste:
        
        if i[0] == set():
            liste_none.append(i)
        else:
            liste_traitement.append([list(i[0]), i[1]])



    liste_secondaire = []
    for i in liste_traitement:
        attention = False

        if len(i[0]) == 1:
            attention = True
        
        for j in i[0]:
            j = j[1:]
            if j[-1] == ".":
                j = j[:-1]

            c = 0
            for lettre in j:
                if lettre == "@":
                    try:
                        lever_exception = j[c + 1]
                        liste_secondaire.append([j, i[1][1]])
                    except IndexError:
                        if attention is True:
                            liste_none.append(i)
                        
                c += 1
                        
            

    for i in liste_secondaire:
        for j in liste_secondaire:

            if i == j:
                liste_secondaire.remove(i)


    for i in liste_secondaire:
        print(i)


    return liste_secondaire, liste_none
    #FAUT RECUPERER L'INTITULER MTN AVEC
    #FONCTION TITRE
    #ON MET AUSSI LA LISTE DES NONE AU CAS OU
    #FAUT Y REFKECGUR





























#FAUT PRECISER LE NUMERO DE LOFFRE
#https://candidat.pole-emploi.fr/offres/recherche/detail/9542526
#DOUBLE ANONCE
