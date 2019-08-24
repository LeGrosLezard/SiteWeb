import requests
from bs4 import BeautifulSoup

def identification_du_site(path):
    """Ici on récupere le nom du site via l'alt de l'image
    sur laquelle on appuie s'il n'y a pas de contact email"""


    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.findAll("div",{"class":"modal-apply"})

    liste = []
    for i in propriete:
        liste.append(str(i.a.img))


    nom = ""
    c = 0
    ok = False
    liste_appening = []
    for i in liste:
        for j in i:
            if i[c] == "s" and\
               i[c + 1] == "i" and\
               i[c + 2] == "t" and\
               i[c + 3] == "e" and\
               i[c + 4] == " ":
                ok = True

            if ok is True:
                nom += i[c]

            if i[c] == '"':
                ok = False
                liste_appening.append(nom)
                nom = ""

            c += 1

    liste_appening1 = []
    
    for i in liste_appening:
        if i == "":
            pass
        else:
            liste_appening1.append(i)


    try:
        return liste_appening1[0][5:-1]
    except IndexError:
        return None

