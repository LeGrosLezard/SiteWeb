from .database.recuperation_document import recuperation_cv


def traitement_cv(pseudo):
    cv = recuperation_cv(pseudo)

    liste = [[],[],[],[],[],[]]

    c = 0
    for i in cv:
        liste[c].append(i)
        c += 1

    c = 0
    for i in liste:
        if liste[c] == []:
            liste[c].append([""])
        c += 1

 
    return liste
