import os

path_doc = r"C:\Users\jeanbaptiste\Desktop\site_travail\environement_virtuel\projetto\static\espace_user\{}"


def controle(dictionnaire_document):

    liste = []
    
    for cle, valeur in dictionnaire_document.items():
        if valeur == 1:
            liste.append(1)
        else:
            liste.append(0)
            
    return liste

def document(user):
    
    liste_os = os.listdir(path_doc.format(user))

    doc = ["cv.pdf", "bilan.pdf", "message.pdf",
           "partie_une_bilan_" + user + ".pdf",
           "partie_deux_bilan_" + user + ".pdf",
           "partie_trois_bilan_" + user + ".pdf",]

    dictionnaire_document = {}

    for i in doc:
        dictionnaire_document[i[:-4]] = 0

    for i in liste_os:
        for cle, valeur in dictionnaire_document.items():
            if i[:-4] == cle:
                dictionnaire_document[cle] += 1

    liste = controle(dictionnaire_document)
    
    return liste[0], liste[1], liste[2], liste[3], liste[4], liste[5]



    

