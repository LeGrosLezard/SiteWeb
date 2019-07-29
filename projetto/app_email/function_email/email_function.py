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
        liste_w = []
        liste_w.append(str(i.a))
        url = ""
        
        for i in liste_w:
            c = 0
            ok = False
            for j in i:
                if i[c] == "h" and i[c + 1] == "r" and i[c + 2] == "e"\
                   and i[c + 3] == "f":
                    ok = True
                    c += 3
                
                if ok is True:
                    if j == " ":
                        pass
                    else:
                        url += j
                
                else:
                    c += 1

                if ok is True and j == " ":
                    liste_w1.append(url[6:-1])
                    break
                


    return liste_w1

    #ICI IL FAUT ABSOLUMENT FAIRE UN RETOUR AJAX PUIS
    #~RENVOYER UN AUTRE CALL





pole_emploi("paris", "développeur", "20")


def second_call():
            
##        path = PATH_POLE_2.format(suite)
##        request_html = requests.get(path)
##        page = request_html.content
##        soup_html = BeautifulSoup(page, "html.parser")
    pass













