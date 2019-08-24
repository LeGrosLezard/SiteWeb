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
