def resultat_function(resultat):
    
    liste = []
    nombre = []
    
    nb = ""
    reponse = ""
    
    
    for i in resultat:

        if i == ",":
            nombre.append(nb)
            liste.append(reponse)
            reponse = ""
            nb = ""
            
        try:
            i = int(i)
            if i == int(i):
                nb += str(i)
        except:
            if i == ",":
                pass
            else:
                reponse += i

    liste.append(reponse)



    final = []

    c = 0
    for i in nombre:
        if i == "":
            pass
        else:
            final.append([i, liste[c+1]])

        c+=1

    return final
    

from .CONFIG import MEMOIRE
def correction(result):
    
    compteur = 0
    for i in result:
        for cle, valeur in MEMOIRE.items():
            if int(i[0]) == cle:
                if i[1] == valeur:
                    compteur += 1
    return compteur










    
