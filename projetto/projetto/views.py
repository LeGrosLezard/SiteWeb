from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import get_template
from django import forms
from django.http import HttpResponse
from django.views.generic import View


from django.contrib.auth import login as lo 
from django.contrib.auth.models import User

from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout

from django.shortcuts import render, redirect

from .forms import compte_utilisateur_form
from .forms import userloginform
from .forms import userregisterform

from .models import compte

#FAUT FAIRE LA DECONNEXTION ET DONC LA GLOBAL


GLOBAL = []

def home(request):
    global GLOBAL
    user = request.user
    print(user)

    if request.method == "POST":
        verification = request.POST.get('verification')

        if verification:
            print("000000000000000000000000000000000000000000000000")

            #FAUT CHECK SI LE MEC A UN BILAN SI OUI RENVOYER OUI ET DONC
            #SUR COMPTE
            #SINON ON LENVOIE SUR LA PAGE BILAN
    
    try:
        return render(request, 'home.html', {"user":GLOBAL[0][0]})
    except IndexError:
        return render(request, 'home.html')

    #On essais de voir si l'utilisateur est connecter ou pas.







def compte(request):
    global GLOBAL

    

    if request.method == "POST":
        
        demande_de_cv = request.POST.get('demande_de_cv')
        demande_de_motivation = request.POST.get('demande_de_motivation')
        demande_de_message = request.POST.get('demande_de_message')


        if demande_de_cv:
            return JsonResponse({"a":"connected"})


        if demande_de_message:
            pass

        if demande_de_motivation:
            pass


    return render(request, 'compte.html')








def questionnaire(request):
    return render(request, 'questionnaire.html')







#We insert document into database here
from .cv.traitement_document import traitement_cv
from .cv.traitement_document import traitement_motivation
from .cv.traitement_document import traitement_message

#
from .cv.database.insertion_document_cv import insertion_part_cv
from .cv.database.insertion_document_motivation import insertion_part_motivation
from .cv.database.insertion_document_message import insertion_part_message

#We recup traitment data
from .cv.database.recuperation_document import recuperation_bilan
from .cv.database.recuperation_document import recuperation_nom
from .cv.database.recuperation_document import recuperation_bilan
from .cv.database.recuperation_document import recuperation_motivation

from .cv.CONFIG import cv1
def comment_faire_mon_cv(request):

    try:

        pseudo = request.user

        nom, prenom = recuperation_nom(pseudo)
        
        cv = traitement_cv(pseudo)


        motivation = traitement_motivation(pseudo)
        message = traitement_message(pseudo)
        print(cv)
        print("")
        print(message)
        
        bilan = recuperation_bilan(pseudo)

    except IndexError:
        pass
    

    if request.method == "POST":
        
        
        motive = request.POST.get('motive')
        message_requete = request.POST.get('message')

        

        if message_requete:
            #PARTIE MESSAGE RECRUTEUR
            print("OUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
            un = request.POST.get('un')
            if un:
                insertion_part_message(pseudo, un, "un")
            
            deux = request.POST.get('deux')
            if deux:
                insertion_part_message(pseudo, deux, "deux")
            
            trois = request.POST.get('trois')
            if trois:
                insertion_part_message(pseudo, trois, "trois")
            
            quattre = request.POST.get('quattre')
            if quattre:
                insertion_part_message(pseudo, quattre, "quattre")
            
            cinq = request.POST.get('cinq')
            if cinq:
                insertion_part_message(pseudo, cinq, "cinq")
            
            six = request.POST.get('six')
            if six:
                insertion_part_message(pseudo, six, "six")





        elif motive:
            #PARTIE LETTRE DE MOTIVATION

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



        
        else:
            #PARTIE CURRICULUM VITAE
            #On récupere l'étape qui correspond au cv
            #et on l'insert dans la database cv, cv1, cv2 ect...
            #Par contre blem : si le mec commence a l'étape 2 ?
            un = request.POST.get('un')
            if un:
                insertion_part_cv(pseudo, un, "un")

            metier = request.POST.get('metier')
            if metier:
                insertion_part_cv(pseudo, metier, "metier")

            formation = request.POST.get('formation')
            if formation:
                insertion_part_cv(pseudo, formation, "formation")
  
            deux = request.POST.get('deux')
            if deux:
                insertion_part_cv(pseudo, deux, "deux")
            
            trois = request.POST.get('trois')
            if trois:
                insertion_part_cv(pseudo, trois, "trois")
            
            quattre = request.POST.get('quattre')
            if quattre:
                insertion_part_cv(pseudo, quattre, "quattre")
            
            cinq = request.POST.get('cinq')
            if cinq:
                insertion_part_cv(pseudo, cinq, "cinq")
            
            six_un = request.POST.get('six_un')
            if six_un:
                insertion_part_cv(pseudo, six_un, "six_un")

            poste1 = request.POST.get('poste1')
            if poste1:
                insertion_part_cv(pseudo, poste1, "poste1")

            six_deux = request.POST.get('six_deux')
            if six_deux:
                insertion_part_cv(pseudo, six_deux, "six_deux")

            poste2 = request.POST.get('poste2')
            if poste2:
                insertion_part_cv(pseudo, poste2, "poste2")


            six_trois = request.POST.get('six_trois')
            if six_trois:
                insertion_part_cv(pseudo, six_trois, "six_trois")

            poste3 = request.POST.get('poste3')
            if poste3:
                insertion_part_cv(pseudo, poste3, "poste3")

            sept = request.POST.get('sept')
            if sept:
                insertion_part_cv(pseudo, sept, "sept")
                




    try:

    
        return render(request, 'comment_faire_mon_cv.html', {"nom" : nom,
                                                             "prenom": prenom,
                                                             "cv1": cv[0],
                                                             "cv2": cv[1],
                                                             "cv3": cv[2],
                                                             "cv4": cv[3],
                                                             "cv5": cv[4],
                                                             "cv6_1": cv[5],
                                                             "cv6_2": cv[6],
                                                             "cv6_3": cv[7],
                                                             "cv7": cv[8],
                                                             "metier": cv[9],
                                                             "formation":cv[10],
                                                             "poste1":cv[11],
                                                             "poste2":cv[12],
                                                             "poste3":cv[13],
                                                             "bilan": bilan,
                                                             "motiv1": motivation[0],
                                                             "motiv2": motivation[1],
                                                             "motiv3": motivation[2],
                                                             "motiv4": motivation[3],
                                                             "motiv5": motivation[4],
                                                             "motiv6": motivation[5],
                                                             "code":  motivation[6],
                                                             "ville":  motivation[7],
                                                             "poste_motivation":  motivation[8],
                                                             "mess1": message[0],
                                                             "mess2": message[1],
                                                             "mess3": message[2],
                                                             "mess4": message[3],
                                                             
                                                             })


    except:
        return render(request, 'comment_faire_mon_cv.html')


def ma_demarche(request):
    return render(request, 'ma_demarche.html')

def le_questionnaire(request):
    return render(request, 'le_questionnaire.html')



from .questionnaire.questionnaire import question_reponse
from .questionnaire.analyse import analyse_questionnaire
from .questionnaire.analyse import association_definition
from .questionnaire.analyse import association_definition1
def le_questionnaire_premiere_partie(request):

    if request.method == "POST":

        questionnaire = request.POST.get('questionnaire')
        print(questionnaire,"00000000000000000000000000000000000000")
        questionnaire_traitee = question_reponse(questionnaire)
        analyse = analyse_questionnaire(questionnaire_traitee)
        reponse = association_definition(analyse)
        reponse_associee = association_definition1(reponse[0], reponse[1])
    return render(request, 'le_questionnaire_premiere_partie.html')





def le_questionnaire_seconde_partie(request):
    return render(request, 'le_questionnaire_seconde_partie.html')

def le_questionnaire_troisieme_partie(request):
    return render(request, 'le_questionnaire_troisieme_partie.html')

def le_questionnaire_quatrieme_partie(request):
    return render(request, 'le_questionnaire_quatrieme_partie.html')




from .cv.traitement_document import traitement_cv
from .cv.traitement_document import traitement_motivation
from .cv.traitement_document import traitement_message
from .cv.database.recuperation_info import recuperation_info
def page_cv(request):

    try:
        pseudo = request.user

        cv = traitement_cv(pseudo)

        nom, prenom, addresse, fixe, portable, email = recuperation_info(pseudo)
        nom = nom.upper()
        prenom = prenom.upper()


        return render(request, 'page_cv.html',
                      {"cv1" : cv[0],
                       "cv2" : cv[1],
                       "cv3" : cv[2],
                       "cv4" : cv[3],
                       "cv5" : cv[4],
                       "cv6" : cv[5],
                       "nom": nom,
                       "prenom": prenom,
                       "addresse": addresse,
                       "fixe": fixe,
                       "portable": portable,
                       "email": email}
                      )

    except IndexError :
        return render(request, 'page_cv.html')
            




    return render(request, 'page_cv.html')


def page_motivation(request):
    return render(request, 'page_motivation.html')



##    motivation = traitement_motivation(pseudo)
##    mesasge = traitement_message(pseudo)
##                   "motvation1" : motivation[0],
##                   "motvation2" : motivation[1],
##                   "motvation3" : motivation[2],
##                   "motvation4" : motivation[3],
##                   "motvation5" : motivation[4],
##                   "motvation6" : motivation[5],
##                   "message1" : mesasge[0],
##                   "message2" : mesasge[1],
##                   "message3" : mesasge[2],
##                   "message4" : mesasge[3],
##                   "message5" : mesasge[4],
##                   "message6" : mesasge[5],





def page_message(request):
    return render(request, 'page_message.html')





