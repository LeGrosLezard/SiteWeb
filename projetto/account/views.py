"""We recup data from user for connexion and registry
We take orm and psycopg2 why ???
We take orm for the connexion aspect.
And psycopg2 (heroku serveur database)
for the rest.
I just prefere the sql but i can orm PROJET8 is only
acces on orm django"""


from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import login as lo 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm
from .models import *



def login_view(request):
    """Here we define the login view"""

    next = request.GET.get('next')
    #We call login form
    form = UserLoginForm(request.POST or None)
    #If form is valid so we
    if form.is_valid():
        #try to recup username and password
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        #With this informations we connect the user.
        user = authenticate(username=username, password=password)
        login(request, user)
        #And we redirect him to home page.
        if next:
            return redirect(next)
        return redirect('../../')
    #Login template with login form.
    return render(request, 'login.html', {'form':form})


def register(request):
    """First part of the registry"""

    next = request.GET.get('next')
    #We call registry form
    form = UserRegisterForm(request.POST or None)
    #If form is valid
    if form.is_valid():
        #We dont save yet into orm user
        user = form.save(commit=False)
        #We cleanning password and email
        passwordd = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        #We define password of user
        user.set_password(passwordd)
        #We saving user
        user.save()
        #And authentificate this new user.
        new_user = authenticate(username=user.username, password=passwordd)
        login(request, new_user)
        #Finnally we redirect him to register part2
        if next:
            return redirect(next)
        return redirect('/account/register2')

    return render(request, 'register.html', {'form':form})



from .compte.compte import inscription
from .compte.compte import creation_dossier_user
def register2(request):
    """Second part of the registry"""
    #If user post
    if request.method == "POST":
        #We try recup inscriptionn
        inscriptionn = request.POST.get('inscriptionn')
        #If there is inscription so
        if inscriptionn:

            current_user = request.user
            #We recup from orm first information
            #Indeed we get orm for connexion
            #We get psycopg2 for the rest
            #i'ts for training ive PROJET8
            #who is only acces on orm
            user = User.objects.get(username=current_user)
            password = user.password
            email = user.email
            pseudo = user.username
            #We recup information from template
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            date = request.POST.get('date')
            sexe = request.POST.get('sexe')
            portable = request.POST.get('portable')
            fixe = request.POST.get('fixe')
            adresse = request.POST.get('adresse')
            #We put this informations into database
            info_inscription = inscription(pseudo,
                                            nom, prenom,
                                            date, sexe, email,
                                            portable, fixe,
                                            adresse,
                                            str(password))
            #Finnaly we create folder user.
            creation_dossier_user(pseudo)


    return render(request, 'register2.html')



login_required
def logout_view(request):
    """Here we define logout session"""

    logout(request)
    print("déconnexion")
    return redirect('/')
