import os

path_doc = r"C:\Users\jeanbaptiste\Desktop\site_travail\environement_virtuel\projetto\static\espace_user\{}"

def controle(dictionnaire_document):
    """We controlling documents of user"""

    liste = []
    for cle, valeur in dictionnaire_document.items():
        if valeur == 1:
            liste.append(1)
        else:
            liste.append(0)
            
    return liste



def document(user):
    """Each users have 4 documents, each user have a folder
    so we go found it !"""

    #we dress list of this folder
    liste_os = os.listdir(path_doc.format(user))
    #We dress list of all document
    doc = ["cv.pdf", "bilan.pdf", "message.pdf",
           "partie_une_bilan_" + user + ".pdf",
           "partie_deux_bilan_" + user + ".pdf",
           "partie_trois_bilan_" + user + ".pdf",]

    dictionnaire_document = {}

    #We initializing dictionnary of the "all document"
    for i in doc:
        dictionnaire_document[i[:-4]] = 0
    #If list of path user and list of all doc matching
    #We add + 1 do dictionnary
    for i in liste_os:
        for cle, valeur in dictionnaire_document.items():
            if i[:-4] == cle:
                dictionnaire_document[cle] += 1
                
    #Thx to that we can say if user has passed or not test
    #if yes he can't passe it
    liste = controle(dictionnaire_document)

    return liste[0], liste[1], liste[2], liste[3], liste[4], liste[5]





#- First - Recup data from database.
from .cv.database.recuperation_document import recuperation_nom
from .cv.database.recuperation_document import recuperation_bilan
from .cv.database.recuperation_document import recuperation_motivation

#- Second -  we must traiting datab.
from .cv.traitement_document import traitement_cv
from .cv.traitement_document import traitement_motivation
from .cv.traitement_document import traitement_message

#- Third - we group it
def documents_user_views(pseudo):
    
    nom, prenom = recuperation_nom(pseudo)
    cv = traitement_cv(pseudo)
    motivation = traitement_motivation(pseudo)
    message = traitement_message(pseudo)

    #- Fourth - We collect it in dictionnary
    data = {"nom" : nom, "prenom": prenom, "cv1": cv[0],
             "cv2": cv[1], "cv3": cv[2], "cv4": cv[3],
             "cv5": cv[4], "cv6_1": cv[5], "cv6_2": cv[6],
             "cv6_3": cv[7], "cv7": cv[8], "metier": cv[9],
             "formation":cv[10], "poste1":cv[11], "poste2":cv[12],
             "poste3":cv[13], "motiv1": motivation[0], "motiv2": motivation[1],
             "motiv3": motivation[2],  "motiv4": motivation[3],
             "motiv5": motivation[4], "motiv6": motivation[5],
             "code":  motivation[6], "ville":  motivation[7],
             "poste_motivation":  motivation[8], "mess1": message[0],
             "mess2": message[1], "mess3": message[2], "mess4": message[3]}

    #- Fifty - we send it to template.
    return nom, prenom, cv, motivation, message, data





from .cv.database.insertion_document_message import insertion_part_message
def insertion_message_views(request, pseudo):

    #We initialise list
    liste = ["un", 'deux', 'trois', 'quattre', 'cinq', 'six']

    #For i in liste if a POST request is askin
    #We try to match with one of this element
    #If yes we insert it into database
    for i in liste:
        asking = request.POST.get(str(i))
        if asking:
            insertion_part_message(pseudo, asking, str(i))


from .cv.database.insertion_document_motivation import insertion_part_motivation
def insertion_motivation_views(request, pseudo):
    """Insertion motvation in database"""

    liste = ["poste_motivation", "ville", "code", "un",
             "deux", "trois", "quattre", "cinq", "six"]

    for i in liste:
        demande = request.POST.get(str(i))
        if demande:
            insertion_part_motivation(pseudo, demande, str(i))
 



from .cv.database.insertion_document_cv import insertion_part_cv
def insertion_cv_views(request, pseudo):
    """Insertion CV in database"""

    liste = ["un", "metier", "formation", "deux", "trois", "quattre", "cinq",
             "six_un", "poste1", "six_deux", "poste2", "six_trois", "poste3",
             "sept"]

    for i in liste:
        demande = request.POST.get(str(i))
        if demande:
            insertion_part_cv(pseudo, demande, str(i))
            
