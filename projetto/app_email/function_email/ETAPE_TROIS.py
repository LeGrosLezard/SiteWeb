import requests
from bs4 import BeautifulSoup


def titre(path):
    """On récupere le titre"""
    print(path)
    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.findAll("h1",{"class":"t2 title"})

    liste = []
    for i in propriete:
        liste.append(str(i.string.lower()))
        
    return liste




from CONFIG import PATH_POLE_2
def verification_metier(liste, ville, emploi_utilisateur):
    """Ici on va voir si le titre == la recherche emploie
    de l'utilisateur

    On va aussi essayer de récupérer l'entreprise qui
    veut recruter.
    """

    emploi_utilisateur = emploi_utilisateur.split()
    liste_ok = []

    for i in liste:
        nom = titre(i)
        
        compteur = 0
        for em in emploi_utilisateur:
            find = str(nom).find(str(em))
            if find >= 0:
                compteur += 1

        if compteur >= len(emploi_utilisateur) - 1:
            liste_ok.append(i)
            
    
    return liste_sauvegarde




























