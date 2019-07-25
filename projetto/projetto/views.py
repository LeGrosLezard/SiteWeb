from django.shortcuts import render
from django.http import JsonResponse



def home(request):
    return render(request, 'home.html')



GLOBAL_CONNEXION = []
from .compte.compte import inscription
from .compte.compte import connexion
from .compte.base_de_donnee.connexion import verifier_connexion
from .compte.base_de_donnee.connexion import user_connected
def compte(request):

    if request.method == "POST":

        inscription_user = request.POST.get('inscription')
        connexion_user = request.POST.get('connexion')

        if inscription_user:
        
            pseudo = request.POST.get('pseudo')
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            date = request.POST.get('date')
            sexe = request.POST.get('sexe')
            email = request.POST.get('email')
            portable = request.POST.get('portable')
            fixe = request.POST.get('fixe')
            adresse = request.POST.get('adresse')
            password = request.POST.get('mot_de_passe')

            info_inscription = inscription(pseudo, nom, prenom,
                                            date, sexe, email,
                                            portable, fixe,
                                            adresse, password)


        if connexion_user:

            password_connexion = request.POST.get('password_connexion')
            pseudo_connexion = request.POST.get('pseudo_connexion')


            pseudo_verif, password_verif = verifier_connexion(pseudo, password)

            if pseudo_verif == pseudo_connexion and\
               password_connexion == password_verif:
                connexion(password_connexion, pseudo_connexion, GLOBAL_CONNEXION)
                



        if verification_user_connexion:

            pseudo_connected, password_connected = user_connected(GLOBAL_CONNEXION)
            if pseudo_connected and password_connected:
                return JsonResponse("connected")




        if deconnexion_user:
            
            GLOBAL_CONNEXION = []







    return render(request, 'compte.html')






def questionnaire(request):
    return render(request, 'questionnaire.html')

def comment_faire_mon_cv(request):
    return render(request, 'comment_faire_mon_cv.html')

def mon_apparence(request):
    return render(request, 'mon_apparence.html')

def ma_demarche(request):
    return render(request, 'ma_demarche.html')

def le_questionnaire(request):
    return render(request, 'le_questionnaire.html')
