from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse


from django import forms

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

def comment_faire_mon_cv(request):
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




from .cv.cv import recuperation_info
def page_cv(request):

##    pseudo = request.user
##    nom, prenom, bilan, motivation = recuperation_info(pseudo)
##    data = {"nom": nom,
##            "prenom": prenom,
##            "bilan": bilan,
##            "motivation": motivation
##            }



##    deja1 = ""
##    deja2 = ""
##    deja3 = ""
##    deja4 = ""
##    deja5 = ""
##    deja6 = ""
##    premier = ""
##    deuxieme = ""
##    troisieme = ""
##    quatrieme = ""
##    cinquieme =""
##    sixieme =  ""
    







    
    ##return render(request, 'page_cv.html', data)

    return render(request, 'page_cv.html')


def ma_lettre(request):
    return render(request, 'ma_lettre.html')

def mon_message(request):
    return render(request, 'mon_message.html')







