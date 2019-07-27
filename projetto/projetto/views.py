from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

#FAUT FAIRE LA DECONNEXTION ET DONC LA GLOBAL


GLOBAL = []

def home(request):
    global GLOBAL
    print(GLOBAL, "UTILISATEUR CONNECTE")

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
        
        demande_de_cv = request.POST.get('demande_de_cv')
        demande_de_motivation = request.POST.get('demande_de_motivation')
        demande_de_message = request.POST.get('demande_de_message')




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




        if demande_de_cv:
            return JsonResponse({"a":"connected"})


        if demande_de_message:
            pass


        if demande_de_motivation:
            pass



















    try:
        return render(request, 'compte.html', {"user":GLOBAL[0][0]})
    except IndexError:
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

    pseudo = request.user
    nom, prenom, bilan, motivation = recuperation_info(pseudo)
    data = {"nom": nom,
            "prenom": prenom,
            "bilan": bilan,
            "motivation": motivation
            }
    
    return render(request, 'page_cv.html', data)




def ma_lettre(request):
    return render(request, 'ma_lettre.html')

def mon_message(request):
    return render(request, 'mon_message.html')







