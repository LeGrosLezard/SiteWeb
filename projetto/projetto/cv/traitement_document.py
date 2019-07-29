"""Here we trating data from database"""

def traitement(data):
    """Here we traiting data from cv table"""

    liste = []

    for i in data[0]:
        if i == None:
            pass
        else:
            liste.append(i)

    if len(liste) < 6:
        a = ['','','','','','']
        liste += a

    return liste





from .database.recuperation_document_cv import recuperation_cv
def traitement_cv(pseudo):
    try:
        cv = recuperation_cv(pseudo)
        liste = traitement(cv)
    except IndexError:
        liste = ['','','','','','']
    return liste



from .database.recuperation_document_motivation import recuperation_motivation
def traitement_motivation(pseudo):
    try:
        motivation = recuperation_motivation(pseudo) 
        liste = traitement(motivation)
    except IndexError:
        liste = ['','','','','','']

    return liste


from .database.recuperation_document_message import recuperation_message
def traitement_message(pseudo):
    try:
        message = recuperation_message(pseudo)
        liste = traitement(message)
        print(liste)
    except IndexError:
        liste = ['','','','','','']

    return liste







