from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import get_template
from django import forms
from django.http import HttpResponse
from django.views.generic import View


from django.contrib.auth import login as lo 
from django.contrib.auth.models import User

from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.generic import View
from django.shortcuts import render, redirect


from django.template.loader import get_template
import pdfkit
from .forms import compte_utilisateur_form
from .forms import userloginform
from .forms import userregisterform

from .models import compte



from .utils import render_to_pdf
from .cv.traitement_document import traitement_cv
from .cv.traitement_document import traitement_motivation
from .cv.traitement_document import traitement_message
from .cv.database.recuperation_info import recuperation_info
from .cv.verify_document import verify_document_cv




from .views_function import document
def home(request):
    """Home template"""
    #In case user is connected
    try:

        pseudo = request.user
        #Ask data from database
        cv, motivation, message, bilan1, bilan2, bilan3 = document(str(pseudo))
        #We need this for inform user if he has completed this or not
        data = {"cv":cv, "motivation":motivation,  "message":message,
                "bilan1":bilan1, "bilan2":bilan2,  "bilan3":bilan3}
        
        return render(request, 'home.html', data)
    #In case user is not connected
    except:
        return render(request, 'home.html')





from .compte.compte import compte_function
def compte(request):

    try:
        pseudo = request.user
        #We ask database for information from the current user.
        info = compte_function(pseudo)

        dico_info = {"nom":"", "prenom":"", "sexe":"", "address_email":"",
                     "fixe":"", "portable":"", "mot_de_passe":"", "pseduo":"",
                     "adresse":"", "naissance":""}   

        c = 1

        for cle, valeur in dico_info.items():
            dico_info[cle] = info[0][c]
            c += 1
        
        if request.method == "POST":
            
            pass


        return render(request, 'compte.html', {"info":dico_info})

    except:
        return render(request, 'compte.html')






def questionnaire(request):
    return render(request, 'questionnaire.html')







from .views_function import documents_user_views
from .views_function import insertion_message_views
from .views_function import insertion_cv_views
from .views_function import insertion_motivation_views
def comment_faire_mon_cv(request):

    try:
        #Trying to recup data of user
        pseudo = request.user
        nom, prenom, cv, motivation, message, data = documents_user_views(pseudo)
    except:
        pass

    if request.method == "POST":
        motive = request.POST.get('motive')
        message_requete = request.POST.get('message')

        if message_requete:
            #Insertion message
            insertion_message_views(request, pseudo)

        elif motive:
            #Insertion motication
            insertion_motivation_views(request, pseudo)

        else:
            #Insertion Cv
            insertion_cv_views(request, pseudo)

    try:#In case we can't recup data from user                               
        return render(request, 'comment_faire_mon_cv.html', data)

    except:
        return render(request, 'comment_faire_mon_cv.html')



def ma_demarche(request):
    return render(request, 'ma_demarche.html')

def le_questionnaire(request):
    return render(request, 'le_questionnaire.html')

from .CONFIG import PATH_DOSSIER_DOCUMENT
def path_dossier_document(request, nom):
    pseudo = request.user
    fichier_uti = str(pseudo) + nom
    return PATH_DOSSIER_DOCUMENT.format(fichier_uti)

def page_cv_pdf(request):
    path = path_dossier_document(request, "\cv.pdf")
    return render(request, 'page_cv_pdf.html', {"path":path})

def page_motivation_pdf(request):
    path = path_dossier_document(request, "\motivation.pdf")
    return render(request, 'page_motivation_pdf.html', {"path":path})

def page_message_pdf(request):
    path = path_dossier_document(request, "\message.pdf")
    return render(request, 'page_message_pdf.html', {"path":path})

def page_bilan_pdf(request):
    path1 = path_dossier_document(request, "\partie_une_bilan_grossebouille.pdf")
    path2 = path_dossier_document(request, "\partie_deux_bilan_grossebouille.pdf")
    path3 = path_dossier_document(request, "\partie_trois_bilan_grossebouille.pdf")
    data = {"path1":path1, "path2":path2, "path3":path3}
    return render(request, 'page_bilan_pdf.html', data)


from .questionnaire.questionnaire import question_reponse
from .questionnaire.questionnaire import analyse_questionnaire
from .questionnaire.questionnaire import association_definition
from .questionnaire.questionnaire import association_definition1
from .questionnaire.questionnaire import association_definition2
from .questionnaire.questionnaire import assoc_grande_categorie
from .questionnaire.questionnaire import mise_en_page
from .questionnaire.database.database import insertion_bilan_premiere_partie
from .views_function import document
from .questionnaire.database.database import accord

def le_questionnaire_premiere_partie(request):

    pseudo = request.user

    #Here we verify if user hsn't passed the form
    ok = accord(pseudo, "un")

    if ok == 1:
        
        cv, motivation, message, bilan1, bilan2, bilan3 = document(str(pseudo))
        data = {"cv":cv,  "motivation":motivation, "message":message,
                "bilan1":bilan1, "bilan2":bilan2, "bilan3":bilan3,
                "avertisseur":"Vous avez déja valider votre bilan psychologique !"}

        return render(request, 'home.html', data)


    if request.method == "POST":

        #- First - We recup POST request
        questionnaire = request.POST.get('questionnaire')
        questionnaire_traitee = question_reponse(questionnaire)

        # - Second - We analysing it (trait respons, just or false)
        analyse = analyse_questionnaire(questionnaire_traitee)
        reponse = association_definition(analyse)
        reponse_associee = association_definition1(reponse)
        reponse_associee2 = association_definition2(reponse)

        # - Third - We constituing analysis
        grande_cat = assoc_grande_categorie(reponse_associee2)
        pagination = mise_en_page(reponse_associee, grande_cat)

        # - Fourth - We insert it into database
        insertion_bilan_premiere_partie(pseudo, pagination)

    return render(request, 'le_questionnaire_premiere_partie.html')



from .views_function import document
from .questionnaire.CONFIG import DICTEE
from .questionnaire.database.database import accord
from .questionnaire.questionnaire_deux import traitement_DICTEE
from .questionnaire.questionnaire_deux import traitement_texte_utilisateur
from .questionnaire.database.database import insertion_bilan_seconde_partie
def le_questionnaire_seconde_partie(request):

    pseudo = request.user

    #Here we verify if user hsn't passed the form
    ok = accord(pseudo, "deux")

    if ok == 1:
        cv, motivation, message, bilan1, bilan2, bilan3 = document(str(pseudo))
        data = {"cv":cv, "motivation":motivation, "message":message,
                "bilan1":bilan1,  "bilan2":bilan2, "bilan3":bilan3,
                "avertisseur":"Vous avez déja valider votre bilan psychologique !"}

        return render(request, 'home.html', data)
    

    if request.method == "POST":

        texte = request.POST.get('texte')

        if texte:
            #Traiting the test
            dictee = traitement_DICTEE(DICTEE)
            
            #Verify the fault
            faute = traitement_texte_utilisateur(texte, dictee)
        
            if faute == None:#There are so many fault we insert no to this test
                insertion_bilan_seconde_partie(pseudo, "non")
            else:#We insert ok to this test
                insertion_bilan_seconde_partie(pseudo, faute)
            
    return render(request, 'le_questionnaire_seconde_partie.html')




from .questionnaire.questionnaire_trois import resultat_function
from .questionnaire.questionnaire_trois import correction_questionnaire3
from .questionnaire.database.database import insertion_bilan_troisieme_partie
from .questionnaire.database.database import accord
from .views_function import document
def le_questionnaire_troisieme_partie(request):

    pseudo = request.user

    #Here we verify if user hsn't passed the form
    acc = accord(pseudo, "trois")

    if acc == 1:
        cv, motivation, message, bilan1, bilan2, bilan3 = document(str(pseudo))
        data = {"cv":cv,  "motivation":motivation, "message":message,
                "bilan1":bilan1, "bilan2":bilan2, "bilan3":bilan3,
                "avertisseur":"Vous avez déja valider votre bilan psychologique !"}

        return render(request, 'home.html', data)
    

    ok = ""
    if request.method == "POST":
        resultat = request.POST.get('resultat')
        
        if resultat:
            correction_uti = resultat_function(resultat)
            la_correction = correction_questionnaire3(correction_uti)

            if la_correction >= 1:
                ok = "L'utilisateur a eu " + str(la_correction) + " à la flexibilité mentale cela veut dire que..."
            else:
                ok = "non"
                
            insertion_bilan_troisieme_partie(pseudo, ok)
            
    return render(request, 'le_questionnaire_troisieme_partie.html')



from .questionnaire.questionnaire_quattre import resultat_function
from .questionnaire.questionnaire_quattre import correction
from .questionnaire.database.database import insertion_bilan_quatrieme_partie
from .questionnaire.database.database import accord
from .views_function import document
def le_questionnaire_quatrieme_partie(request):

    #Here we verify if user hsn't passed the form
    acc = accord(pseudo, "quattre")
    if acc == 1:
        cv, motivation, message, bilan1, bilan2, bilan3 = document(str(pseudo))
        data = {"cv":cv, "motivation":motivation, "message":message,
                "bilan1":bilan1, "bilan2":bilan2, "bilan3":bilan3,
                "avertisseur":"Vous avez déja valider votre bilan psychologique !"}

        return render(request, 'home.html', data)
    

    ok = ""
    pseudo = request.user
    if request.method == "POST":
        resultat = request.POST.get('resultat')

        if resultat:
            result = resultat_function(resultat)
            correct =  correction(result)

            if correct >= 15:
                ok = "La personne a eu plus que la moyenne dans le test de la mémoire ce qui..."
            else:
                ok = "non"

            insertion_bilan_quatrieme_partie(pseudo, ok)
    
    return render(request, 'le_questionnaire_quatrieme_partie.html')




from .cv.traitement_document import traitement_cv
from .cv.traitement_document import traitement_motivation
from .cv.traitement_document import traitement_message
from .cv.database.recuperation_info import recuperation_info

from .forms import DocumentForm_cv
from .models import Document_cv
from .cv.document_user import document_cv_download
def page_cv(request):


    pseudo = request.user
    form = DocumentForm_cv(request.POST, request.FILES)
    ok = False
    
    if request.method == "POST":
        
        if form.is_valid():
            try:
                ok = True
                newdoc = Document_cv(docfile = request.FILES['docfile'])
                newdoc.save()
            except:
                pass
        else:
            pass
 

    if ok is True:
        document_cv_download(pseudo)
        ok = False


    try:
        pseudo = request.user

        cv = traitement_cv(pseudo)

        nom, prenom, addresse, fixe, portable, email = recuperation_info(pseudo)
        nom = nom.upper()
        prenom = prenom.upper()

        data = {"cv1" : cv[0], "cv2" : cv[1], "cv3" : cv[2],
                "cv4" : cv[3], "cv5" : cv[4], "cv6" : cv[5],
                "nom": nom, "prenom": prenom, "addresse": addresse,
                "fixe": fixe, "portable": portable, "email": email,
                "form":form}

        return render(request, 'page_cv.html', data)

    except IndexError :
        return render(request, 'page_cv.html', {"form":form})
            
    return render(request, 'page_cv.html')



from .forms import DocumentForm_motivation
from .models import Document_motivation
from .cv.document_user import document_motivation_download
def page_motivation(request):

    form = DocumentForm_motivation(request.POST, request.FILES)
    pseudo = request.user
    ok = False

    if request.method == "POST":
        
        if form.is_valid():
            try:
                ok = True
                newdoc = Document_motivation(docfile = request.FILES['docfile'])
                newdoc.save()
            except:
                pass
        else:
            pass

    if ok is True:
        document_motivation_download(pseudo)
        ok = False

        
    return render(request, 'page_motivation.html', {"form":form})



from .forms import DocumentForm_message
from .models import Document_message
from .cv.document_user import document_message_download
def page_message(request):


    pseudo = request.user
    ok = False
    
    form = DocumentForm_message(request.POST, request.FILES)

    
    if request.method == "POST":
        
        if form.is_valid():
            try:
                ok = True
                newdoc = Document_message(docfile = request.FILES['docfile'])
                newdoc.save()
            except:
                pass

    if ok is True:
        document_message_download(pseudo)
        ok = False
    
    return render(request, 'page_message.html', {"form":form})



from .questionnaire.database.database import recuperation_info_perso
from .questionnaire.database.database import récupération_psycho
from .questionnaire.database.database import recuperation_dictee
from .questionnaire.database.database import recuperation_flexi
from .questionnaire.database.database import recuperation_memoire

from .forms import DocumentForm_bilan
from .models import Document_bilan
from .cv.document_user import document_bilan_download
def page_bilan(request):

    pseudo = request.user

    nom, prenom = recuperation_info_perso(pseudo)
    bilan1 = récupération_psycho(pseudo)
    bilan2 = recuperation_dictee(pseudo)
    bilan3 = recuperation_flexi(pseudo)
    bilan4 = recuperation_memoire(pseudo)
    

    form = DocumentForm_message(request.POST, request.FILES)

    data = {"nom":nom, "prenom":prenom, "bilan1":bilan1, "bilan2":bilan2,
            "bilan3":bilan3, "bilan4":bilan4, "pseudo":pseudo, "form":form}

    return render(request, 'page_bilan.html', data)



from .forms import DocumentForm_bilan
from .models import Document_bilan
from .cv.document_user import document_bilan_download
def page_bilan1(request):

    pseudo = request.user

    nom, prenom = recuperation_info_perso(pseudo)
    bilan1 = récupération_psycho(pseudo)
    bilan2 = recuperation_dictee(pseudo)
    bilan3 = recuperation_flexi(pseudo)
    bilan4 = recuperation_memoire(pseudo)
    

    ok = False
    
    form = DocumentForm_message(request.POST, request.FILES)

    
    if request.method == "POST":
        
        if form.is_valid():
            try:
                ok = True
                newdoc = Document_bilan(docfile = request.FILES['docfile'])
                newdoc.save()
            except:
                pass

    if ok is True:
        document_bilan_download(pseudo, "partie_une_bilan_" + str(pseudo) + ".pdf")
        ok = False
    


    data = {"nom":nom, "prenom":prenom, "bilan1":bilan1, "bilan2":bilan2,
            "bilan3":bilan3, "bilan4":bilan4, "pseudo":pseudo, "form":form}

    return render(request, 'page_bilan.html', data)




from .forms import DocumentForm_bilan
from .models import Document_bilan
from .cv.document_user import document_bilan_download
def page_bilan2(request):

    pseudo = request.user

    nom, prenom = recuperation_info_perso(pseudo)
    bilan1 = récupération_psycho(pseudo)
    bilan2 = recuperation_dictee(pseudo)
    bilan3 = recuperation_flexi(pseudo)
    bilan4 = recuperation_memoire(pseudo)
    

    ok = False
    
    form = DocumentForm_message(request.POST, request.FILES)

    
    if request.method == "POST":
        
        if form.is_valid():
            try:
                ok = True
                newdoc = Document_bilan(docfile = request.FILES['docfile'])
                newdoc.save()
            except:
                pass

    if ok is True:
        document_bilan_download(pseudo, "partie_deux_bilan_" + str(pseudo) + ".pdf")
        ok = False
    


    data = {"nom":nom, "prenom":prenom, "bilan1":bilan1, "bilan2":bilan2,
            "bilan3":bilan3, "bilan4":bilan4, "pseudo":pseudo, "form":form}

    return render(request, 'page_bilan.html', data)




from .forms import DocumentForm_bilan
from .models import Document_bilan
from .cv.document_user import document_bilan_download
def page_bilan3(request):

    pseudo = request.user

    nom, prenom = recuperation_info_perso(pseudo)
    bilan1 = récupération_psycho(pseudo)
    bilan2 = recuperation_dictee(pseudo)
    bilan3 = recuperation_flexi(pseudo)
    bilan4 = recuperation_memoire(pseudo)

    ok = False
    
    form = DocumentForm_message(request.POST, request.FILES)

    
    if request.method == "POST":
        
        if form.is_valid():
            try:
                ok = True
                newdoc = Document_bilan(docfile = request.FILES['docfile'])
                newdoc.save()
            except:
                pass

    if ok is True:
        document_bilan_download(pseudo, "partie_trois_bilan_" + str(pseudo) + ".pdf")
        ok = False
    


    data = {"nom":nom, "prenom":prenom, "bilan1":bilan1, "bilan2":bilan2,
            "bilan3":bilan3, "bilan4":bilan4, "pseudo":pseudo, "form":form}

    return render(request, 'page_bilan.html', data)








