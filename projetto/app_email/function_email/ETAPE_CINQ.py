import requests
from bs4 import BeautifulSoup

def recherche_entreprise_bas_de_page(path):

    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.findAll("h4", {"class":"t4 title"})
    saut = False
    liste = []
    for i in propriete:
        liste.append(str(i.get_text()))

    if liste == []:
        out = None
    else:
        if liste[0][:2] == "\n" and liste[0][2:] == "\n":
            liste = liste[0][1:-1]
            out = liste
        else:
            out = liste[0]

    try:
        return out
    except IndexError:
        return None
