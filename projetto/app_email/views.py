from django.shortcuts import render
from django.http import HttpResponse


#Here it's for no automatic email
from .views_function import mail_precis_function

#Here we traiting data send by uder(job, localisation)
from .views_function import traitement_reponse
#Here we search all urls who match with our message
from .function_email.recuperation_email import etape_UNE
#Second part
from .function_email.recuperation_email import ETAPE_DEUX
#Third part
from .function_email.recuperation_email import ETAPE_TROIS



LISTE_CONTAINER = []
INFO = []
def questionnaire_email(request):

    global LISTE_CONTAINER
    global INFO
    
    pseudo = request.user
    if request.method == "POST":

        #User enter his mail (he wants send his mail to...)
        mail_precis = request.POST.get('mail_precis')
        #User wants automatic email        
        all_function = request.POST.get('all_function')
        #Second part of automatic functionality
        seconde_partie = request.POST.get('seconde_partie')
        #Third part of automatic functionality
        troisieme_partie = request.POST.get('troisieme_partie')


        #Here it's for mail to one person
        if mail_precis:
            mail_precis_function(request, pseudo)

        #Here it's automatic function mail
        if all_function:
            #Info send by user (job, localisation)
            recherche = request.POST.get('recherche')
            #traiting the informations
            emploi, lieu = traitement_reponse(recherche)
            #Search data on pole emploi
            liste_url_pole = etape_UNE(lieu, emploi, "60")
            #return respons it void time out if void == eviter
            LISTE_CONTAINER.append(liste_url_pole)
            INFO.append([emploi, lieu])
            return HttpResponse(liste_url_pole)

        if seconde_partie:
            recuperation_info = ETAPE_DEUX(LISTE_CONTAINER)
            LISTE_CONTAINER = []
            LISTE_CONTAINER.append(recuperation_info)
            return HttpResponse(recuperation_info)
        
        if troisieme_partie:
            print(LISTE_CONTAINER[0])
            print("")
            print("")
            print("")
            print("")
            
            ETAPE_TROIS(LISTE_CONTAINER[0], INFO[0][1], INFO[0][0])

    return render(request, 'questionnaire_email.html')




def essais(request):
    return render(request, 'essais.html')











