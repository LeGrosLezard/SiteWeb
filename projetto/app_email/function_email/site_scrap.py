import requests
from bs4 import BeautifulSoup


from .CONFIG import PATH_POSTAL
def function_code_postal(lieu):
    """Here we recup the postal code of the current place."""

    path = PATH_POSTAL.format(lieu)

    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.find_all("td")

    code = []
    #We trying it with only one code

    c = 0
    for i in propriete:
        if propriete[c].string == "Code Insee":
            code.append(propriete[c + 1].string)
        c+=1

    if code == []:
        #We trying it with multiple codes.
        for i in range(len(propriete)):
            try:
                numero = int(propriete[i].string)
                code.append(numero)
            except:
                pass

    return code



from .CONFIG import PATH_POLE
def pole_emploi(lieu, emploi, rayon):

    code = function_code_postal(lieu)

    liste_w1 = []
    
    for i in code:

        path = PATH_POLE.format(i, emploi, rayon)

        request_html = requests.get(path)
        page = request_html.content
        soup_html = BeautifulSoup(page, "html.parser")

        propriete = soup_html.findAll("div",{"class":"media"})


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




#------------------------------------------------------------------------
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
    




from .CONFIG import PATH_POLE_2
def verification_metier(liste, ville, LISTE_EMPLOI_UTILISATEUR):
    """Ici on va voir si le titre == la recherche emploie
    de l'utilisateur

    On va aussi essayer de récupérer l'entreprise qui
    veut recruter.
    """

    liste_sauvegarde = []
    b = []
    c = []
    ok = False
    
    
    recuperation1 = titre(liste)

    for i in LISTE_EMPLOI_UTILISATEUR:
        carac = ""
        for j in i:
            if j == " ":
                b.append(carac)
                carac = ""
                
            carac += j

        b.append(carac)


    for i in recuperation1:
        caractere = ""
        for j in i:
            if j == " ":
                c.append(caractere)
                caractere = ""
                
            caractere += j

    for i in c:
        for j in b:
            find = str(i).find(j)
            if find >= 0:
                ok = True


    if ok is True:
        liste_sauvegarde.append(liste)

    
    return liste_sauvegarde


#------------------------------------------------------------------------



def recherche_email(path):
    """Sur le site y'a un un dispositif a l'information
    a gauche, on cherche si ya l'adresse email dans cet onglet"""


    request_html = requests.get(path[0])
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




def recherche_entreprise_bas_de_page(path):

    request_html = requests.get(path[0])
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


def identification_du_site(path):
    """Ici on récupere le nom du site via l'alt de l'image
    sur laquelle on appuie s'il n'y a pas de contact email"""


    request_html = requests.get(path[0])
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



def recherche_via_image(path):
    """Ici c'est comme si on appuyait sur
    l'image dans la description"""

    
    request_html = requests.get(path[0])
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
