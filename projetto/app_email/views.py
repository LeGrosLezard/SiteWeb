from django.shortcuts import render
from django.http import HttpResponse


#Here it's for no automatic email
from .views_function import mail_precis_function

#Here we traiting data send by uder(job, localisation)
from .views_function import traitement_reponse


LISTE_LAPINOU = []

def questionnaire_email(request):

    pseudo = request.user
    if request.method == "POST":

        #User enter his mail (he wants send his mail to...)
        mail_precis = request.POST.get('mail_precis')
        #User wants automatic email        
        all_function = request.POST.get('all_function')
        
        un = request.POST.get('un')
        deux = request.POST.get('deux')
        trois = request.POST.get('trois')
        quattre = request.POST.get('quattre')
        cinq = request.POST.get('cinq')
        six = request.POST.get('six')
        sept = request.POST.get('sept')

        #Here it's for mail to one person
        if mail_precis:
            mail_precis_function(request, pseudo)

        #Here it's automatic function mail
        if all_function:
            #if it's auto so we have data send by user
            recherche = request.POST.get('recherche')
            #we clean it
            emploi, lieu = traitement_reponse(recherche)
            #let's do the first search !!!
            liste_url_pole = etape_UNE(lieu, emploi, "60")
            LISTE_LAPINOU.append(liste_url_pole)
            return HttpResponse("ok")
        






    return render(request, 'questionnaire_email.html')




def essais(request):
    return render(request, 'essais.html')











