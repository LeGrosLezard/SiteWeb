from django.shortcuts import render
from django.http import HttpResponse


#Here it's for no automatic email
from .views_function import mail_precis_function

#Here we traiting data send by uder(job, localisation)
from .views_function import traitement_reponse



def questionnaire_email(request):


    
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

            pass



    return render(request, 'questionnaire_email.html')




def essais(request):
    return render(request, 'essais.html')











