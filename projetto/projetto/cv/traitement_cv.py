from .database.recuperation_document_cv import recuperation_cv


def traitement_cv(pseudo):
    cv = recuperation_cv(pseudo)

    liste = []

    for i in cv[0]:
        if i == None:
            pass
        else:
            liste.append(i)

    if len(liste) < 6:
        a = ['','','','','','']
        liste += a

    return liste
