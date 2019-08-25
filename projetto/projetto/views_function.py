import os

path_doc = r"C:\Users\jeanbaptiste\Desktop\site_travail\environement_virtuel\projetto\static\espace_user\{}"



#We recup traitment data
from .cv.database.recuperation_document import recuperation_bilan
from .cv.database.recuperation_document import recuperation_nom
from .cv.database.recuperation_document import recuperation_bilan
from .cv.database.recuperation_document import recuperation_motivation
def documents_user_views(pseudo):
    
    nom, prenom = recuperation_nom(pseudo)
    cv = traitement_cv(pseudo)
    motivation = traitement_motivation(pseudo)
    message = traitement_message(pseudo)
    bilan = recuperation_bilan(pseudo)

    return nom, cv, motivation, message, bilan




from .cv.database.insertion_document_message import insertion_part_message
def insertion_message_views(request, pseudo):

##    liste = ["un", 'deux', 'trois', 'quattre', 'cinq', 'six']
##
##    for i in liste:
##        asking = request.POST.get(str(i))
##        if asking:
##            insertion_part_message(pseudo, asking, str(i))


#A ESSAYER
            
    un = request.POST.get('un')
    deux = request.POST.get('deux')
    trois = request.POST.get('trois')
    quattre = request.POST.get('quattre')
    cinq = request.POST.get('cinq')
    six = request.POST.get('six')

    if un:
        insertion_part_message(pseudo, un, "un")
    if deux:
        insertion_part_message(pseudo, deux, "deux")
    if trois:
        insertion_part_message(pseudo, trois, "trois")
    if quattre:
        insertion_part_message(pseudo, quattre, "quattre")
    if cinq:
        insertion_part_message(pseudo, cinq, "cinq")
    if six:
        insertion_part_message(pseudo, six, "six")





from .cv.database.insertion_document_motivation import insertion_part_motivation
def insertion_motivation_views(request, pseudo):
    poste_motivation = request.POST.get('poste_motivation')
    if poste_motivation:

        insertion_part_motivation(pseudo, poste_motivation, "poste_motivation")


        ville = request.POST.get('ville')
        if ville:
            insertion_part_motivation(pseudo, ville, "ville")

        code = request.POST.get('code')
        if code:
            insertion_part_motivation(pseudo, code, "code")

        un = request.POST.get('un')
        if un:
            insertion_part_motivation(pseudo, un, "un")
        
        deux = request.POST.get('deux')
        if deux:
            insertion_part_motivation(pseudo, deux, "deux")
        
        trois = request.POST.get('trois')
        if trois:
            insertion_part_motivation(pseudo, trois, "trois")
        
        quattre = request.POST.get('quattre')
        if quattre:
            insertion_part_motivation(pseudo, quattre, "quattre")
        
        cinq = request.POST.get('cinq')
        if cinq:
            insertion_part_motivation(pseudo, cinq, "cinq")
        
        six = request.POST.get('six')
        if six:
            insertion_part_motivation(pseudo, six, "six")





from .cv.database.insertion_document_cv import insertion_part_cv
def insertion_cv_views(request, pseudo):
    un = request.POST.get('un')
    if un:
        insertion_part_cv(pseudo, un, "un")
        verify_document_cv(pseudo)
     
        
    metier = request.POST.get('metier')
    if metier:
        insertion_part_cv(pseudo, metier, "metier")

        
    formation = request.POST.get('formation')
    if formation:
        insertion_part_cv(pseudo, formation, "formation")


    deux = request.POST.get('deux')
    if deux:
        insertion_part_cv(pseudo, deux, "deux")
        verify_document_cv(pseudo)

    
    trois = request.POST.get('trois')
    if trois:
        insertion_part_cv(pseudo, trois, "trois")
        verify_document_cv(pseudo)
       
    
    quattre = request.POST.get('quattre')
    if quattre:
        insertion_part_cv(pseudo, quattre, "quattre")
        verify_document_cv(pseudo)
  
    
    cinq = request.POST.get('cinq')
    if cinq:
        insertion_part_cv(pseudo, cinq, "cinq")
        verify_document_cv(pseudo)
   
    
    six_un = request.POST.get('six_un')
    if six_un:
        insertion_part_cv(pseudo, six_un, "six_un")
        verify_document_cv(pseudo)
        

    poste1 = request.POST.get('poste1')
    if poste1:
        insertion_part_cv(pseudo, poste1, "poste1")

    six_deux = request.POST.get('six_deux')
    if six_deux:
        insertion_part_cv(pseudo, six_deux, "six_deux")
        verify_document_cv(pseudo)
     

    poste2 = request.POST.get('poste2')
    if poste2:
        insertion_part_cv(pseudo, poste2, "poste2")


    six_trois = request.POST.get('six_trois')
    if six_trois:
        insertion_part_cv(pseudo, six_trois, "six_trois")
        verify_document_cv(pseudo)
   

    poste3 = request.POST.get('poste3')
    if poste3:
        insertion_part_cv(pseudo, poste3, "poste3")

    sept = request.POST.get('sept')
    if sept:
        insertion_part_cv(pseudo, sept, "sept")
        verify_document_cv(pseudo)
  



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




