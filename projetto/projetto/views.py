from django.shortcuts import render
from django.http import JsonResponse


GLOBAL = []

def home(request):
    global GLOBAL
    print(GLOBAL, "UTILISATEUR CONNECTE")

    try:
        return render(request, 'home.html', {"user":GLOBAL[0][0]})
    except IndexError:
        return render(request, 'home.html')



from .compte.compte import inscription
from .compte.compte import connexion
from .compte.base_de_donnee.connexion import verifier_connexion
from .compte.base_de_donnee.connexion import user_connected
from .compte.compte import deconnexion
def compte(request):
    global GLOBAL

    print(GLOBAL, "UTILISATEUR CONNECTE")
    if request.method == "POST":

        inscription_user = request.POST.get('inscription')
        connexion_user = request.POST.get('connexion')
        verification_user_connexion = request.POST.get('verification_user_connexion')
        deconnexion_user = request.POST.get('deconnexion_user')


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
            #donc si on requete la connexion

            password_connexion = request.POST.get('password_connexion')
            pseudo_connexion = request.POST.get('pseudo_connexion')
            #on récupere le mdp et le pseudo

            pseudo_verif, password_verif = verifier_connexion(pseudo_connexion,
                                                              password_connexion)
            #on va dans la table users y'a un match ?
    

            if pseudo_verif == pseudo_connexion and\
               password_connexion == password_verif:
                #Si y'a un match
                
                connexion(password_connexion, pseudo_connexion)
                GLOBAL.append([pseudo_verif, password_verif])
                #Si y'a un match, on ajoute les identifiants
                #dans la table connexion
                #mais aussi a global pour les pages
                """Ptetre pas la meilleur soluce"""




        if verification_user_connexion:
            #On verifie la global et la table connection
            print(GLOBAL, "000000000000000000000000000000000000000000")
            pseudo_connected, password_connected = user_connected(GLOBAL[0][0],
                                                                  GLOBAL[0][1])
            
            #On verifie la table connexion mtn !
            if pseudo_connected and password_connected:
                return JsonResponse("connected")




        if deconnexion_user:
            deconnexion(pseudo, password)
            GLOBAL = []




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
