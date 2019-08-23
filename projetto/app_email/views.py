from django.shortcuts import render
from django.http import HttpResponse


#Here it's for no automatic email
from .views_function import mail_precis_function

#Here we search all urls who match with our message
from .function_email.recuperation_email import etape_UNE
from .views_function import traitement_reponse

def questionnaire_email(request):

    pseudo = request.user

    if request.method == "POST":

        mail_precis = request.POST.get('mail_precis')
        all_function = request.POST.get('all_function')

        #Here it's for mail to one person
        if mail_precis:
            mail_precis_function(request, pseudo)


        #Here it's automatic function mail
        if all_function:

            recherche = request.POST.get('recherche')
            
            emploi, lieu = traitement_reponse(recherche)

            liste_url_pole = etape_UNE(lieu, emploi, "60")
            print(liste_url_pole)
            return HttpResponse(liste_url_pole)


            

    return render(request, 'questionnaire_email.html')




def essais(request):
    return render(request, 'essais.html')











