from django.shortcuts import render



def home(request):
    return render(request, 'home.html')



from .compte.compte import inscription
from .compte.compte import connexion
def compte(request):

    if request.method == "POST":

        inscription = request.POST.get('inscription')
        connexion = request.POST.get('connexion')

        if inscription:
        
            pseudo = request.POST.get('pseudo')
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            date = request.POST.get('date')
            sexe = request.POST.get('sexe')
            email = request.POST.get('email')
            portable = request.POST.get('portable')
            fixe = request.POST.get('fixe')
            adresse = request.POST.get('adresse')
            mot_de_passe = request.POST.get('mot_de_passe')

            inscription(pseudo, nom, prenom,
                        date, sexe, email,
                        portable, fixe,
                        adresse, mot_de_passe)


        if connexion:

            password_connexion = request.POST.get('password_connexion')
            pseudo_connexion = request.POST.get('pseudo_connexion')
        
            connexion(password_connexion, pseudo_connexion)






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
