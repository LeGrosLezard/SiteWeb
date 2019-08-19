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


    
    return render(request, 'page_bilan_pdf.html', {"path1":path1,
                                                   "path2":path2,
                                                   "path3":path3})




def home(request):

    pseudo = request.user


    if request.method == "POST":
        verification_document = request.POST.get('verification_document')

        

        if verification_document:
            cv = request.POST.get('un')
            if cv:
                pass

            
            cv_pdf = request.POST.get('unun')
            if cv_pdf:

                verification = verify_document_cv(pseudo, "cv")

                if verification == "verification":

                    return HttpResponse("ok")        
                    


  
                else:
                    return HttpResponse("not_ok")


                


            motivation = request.POST.get('deux')
            if motivation:
                pass
            
            motivation_pdf = request.POST.get('deuxdeux')
            if motivation_pdf:
                verification = verify_document_cv(pseudo, "lettre_de_motivation")
                if verification == "verification":
                    return HttpResponse("ok")
                #retourner page pdf
                else:
                    return HttpResponse("not_ok")

                
        
            message = request.POST.get('trois')
            if message:
                pass
            
            message_pdf = request.POST.get('troistrois')
            if message_pdf:
                verification = verify_document_cv(pseudo, "message")
                if verification == "verification":
                    return HttpResponse("ok")
                else:
                    return HttpResponse("not_ok")


            bilan = request.POST.get('quattre')
            if bilan:
                pass


            bilan_pdf = request.POST.get('quattrequattre')
            if bilan_pdf:
                verification = verify_document_cv(pseudo, "bilan")
                if verification == "verification":
                    return HttpResponse("ok")
                else:
                    return HttpResponse("not_ok")


    

    return render(request, 'home.html')





def compte(request):
    global GLOBAL

    

    if request.method == "POST":
        
        demande_de_cv = request.POST.get('demande_de_cv')
        demande_de_motivation = request.POST.get('demande_de_motivation')
        demande_de_message = request.POST.get('demande_de_message')

        if demande_de_cv:
            return JsonResponse({"a":"connected"})


        if demande_de_message:
            pass

        if demande_de_motivation:
            pass


    return render(request, 'compte.html')








def questionnaire(request):
    return render(request, 'questionnaire.html')







#We insert document into database here
from .cv.traitement_document import traitement_cv
from .cv.traitement_document import traitement_motivation
from .cv.traitement_document import traitement_message

#
from .cv.database.insertion_document_cv import insertion_part_cv
from .cv.database.insertion_document_motivation import insertion_part_motivation
from .cv.database.insertion_document_message import insertion_part_message

#We recup traitment data
from .cv.database.recuperation_document import recuperation_bilan
from .cv.database.recuperation_document import recuperation_nom
from .cv.database.recuperation_document import recuperation_bilan
from .cv.database.recuperation_document import recuperation_motivation

def comment_faire_mon_cv(request):

    try:

        pseudo = request.user

        nom, prenom = recuperation_nom(pseudo)
        
        cv = traitement_cv(pseudo)


        motivation = traitement_motivation(pseudo)
        message = traitement_message(pseudo)

        
        bilan = recuperation_bilan(pseudo)

    except IndexError:
        pass
    

    if request.method == "POST":
        
        
        motive = request.POST.get('motive')
        message_requete = request.POST.get('message')

        

        if message_requete:
            #PARTIE MESSAGE RECRUTEUR
            print("OUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
            un = request.POST.get('un')
            if un:
                insertion_part_message(pseudo, un, "un")
            
            deux = request.POST.get('deux')
            if deux:
                insertion_part_message(pseudo, deux, "deux")
            
            trois = request.POST.get('trois')
            if trois:
                insertion_part_message(pseudo, trois, "trois")
            
            quattre = request.POST.get('quattre')
            if quattre:
                insertion_part_message(pseudo, quattre, "quattre")
            
            cinq = request.POST.get('cinq')
            if cinq:
                insertion_part_message(pseudo, cinq, "cinq")
            
            six = request.POST.get('six')
            if six:
                insertion_part_message(pseudo, six, "six")





        elif motive:
            #PARTIE LETTRE DE MOTIVATION

            poste_motivation = request.POST.get('poste_motivation')
            if poste_motivation:

                insertion_part_motivation(pseudo, poste_motivation, "poste_motivation")


            ville = request.POST.get('ville')
            if ville:
                insertion_part_motivation(pseudo, ville, "ville")

            code = request.POST.get('code')
            if code:
                insertion_part_motivation(pseudo, code, "code")

            un = request.POST.get('un')
            if un:
                insertion_part_motivation(pseudo, un, "un")
            
            deux = request.POST.get('deux')
            if deux:
                insertion_part_motivation(pseudo, deux, "deux")
            
            trois = request.POST.get('trois')
            if trois:
                insertion_part_motivation(pseudo, trois, "trois")
            
            quattre = request.POST.get('quattre')
            if quattre:
                insertion_part_motivation(pseudo, quattre, "quattre")
            
            cinq = request.POST.get('cinq')
            if cinq:
                insertion_part_motivation(pseudo, cinq, "cinq")
            
            six = request.POST.get('six')
            if six:
                insertion_part_motivation(pseudo, six, "six")



        
        else:
            #PARTIE CURRICULUM VITAE
            #On récupere l'étape qui correspond au cv
            #et on l'insert dans la database cv, cv1, cv2 ect...
            #Par contre blem : si le mec commence a l'étape 2 ?
            un = request.POST.get('un')
            if un:
                insertion_part_cv(pseudo, un, "un")
                verify_document_cv(pseudo)
             
                
            metier = request.POST.get('metier')
            if metier:
                insertion_part_cv(pseudo, metier, "metier")

                
            formation = request.POST.get('formation')
            if formation:
                insertion_part_cv(pseudo, formation, "formation")

  
            deux = request.POST.get('deux')
            if deux:
                insertion_part_cv(pseudo, deux, "deux")
                verify_document_cv(pseudo)
   
            
            trois = request.POST.get('trois')
            if trois:
                insertion_part_cv(pseudo, trois, "trois")
                verify_document_cv(pseudo)
               
            
            quattre = request.POST.get('quattre')
            if quattre:
                insertion_part_cv(pseudo, quattre, "quattre")
                verify_document_cv(pseudo)
          
            
            cinq = request.POST.get('cinq')
            if cinq:
                insertion_part_cv(pseudo, cinq, "cinq")
                verify_document_cv(pseudo)
           
            
            six_un = request.POST.get('six_un')
            if six_un:
                insertion_part_cv(pseudo, six_un, "six_un")
                verify_document_cv(pseudo)
                

            poste1 = request.POST.get('poste1')
            if poste1:
                insertion_part_cv(pseudo, poste1, "poste1")

            six_deux = request.POST.get('six_deux')
            if six_deux:
                insertion_part_cv(pseudo, six_deux, "six_deux")
                verify_document_cv(pseudo)
             

            poste2 = request.POST.get('poste2')
            if poste2:
                insertion_part_cv(pseudo, poste2, "poste2")


            six_trois = request.POST.get('six_trois')
            if six_trois:
                insertion_part_cv(pseudo, six_trois, "six_trois")
                verify_document_cv(pseudo)
           

            poste3 = request.POST.get('poste3')
            if poste3:
                insertion_part_cv(pseudo, poste3, "poste3")

            sept = request.POST.get('sept')
            if sept:
                insertion_part_cv(pseudo, sept, "sept")
                verify_document_cv(pseudo)
          




    try:

    
        return render(request, 'comment_faire_mon_cv.html', {"nom" : nom,
                                                             "prenom": prenom,
                                                             "cv1": cv[0],
                                                             "cv2": cv[1],
                                                             "cv3": cv[2],
                                                             "cv4": cv[3],
                                                             "cv5": cv[4],
                                                             "cv6_1": cv[5],
                                                             "cv6_2": cv[6],
                                                             "cv6_3": cv[7],
                                                             "cv7": cv[8],
                                                             "metier": cv[9],
                                                             "formation":cv[10],
                                                             "poste1":cv[11],
                                                             "poste2":cv[12],
                                                             "poste3":cv[13],
                                                             "bilan": bilan,
                                                             "motiv1": motivation[0],
                                                             "motiv2": motivation[1],
                                                             "motiv3": motivation[2],
                                                             "motiv4": motivation[3],
                                                             "motiv5": motivation[4],
                                                             "motiv6": motivation[5],
                                                             "code":  motivation[6],
                                                             "ville":  motivation[7],
                                                             "poste_motivation":  motivation[8],
                                                             "mess1": message[0],
                                                             "mess2": message[1],
                                                             "mess3": message[2],
                                                             "mess4": message[3],
                                                             
                                                             })


    except:
        return render(request, 'comment_faire_mon_cv.html')


def ma_demarche(request):
    return render(request, 'ma_demarche.html')

def le_questionnaire(request):
    return render(request, 'le_questionnaire.html')



from .questionnaire.questionnaire import question_reponse
from .questionnaire.questionnaire import analyse_questionnaire
from .questionnaire.questionnaire import association_definition
from .questionnaire.questionnaire import association_definition1
from .questionnaire.questionnaire import association_definition2
from .questionnaire.questionnaire import assoc_grande_categorie
from .questionnaire.questionnaire import mise_en_page
from .questionnaire.database.database import insertion_bilan_premiere_partie
def le_questionnaire_premiere_partie(request):

    pseudo = request.user


    if request.method == "POST":

        questionnaire = request.POST.get('questionnaire')
        questionnaire_traitee = question_reponse(questionnaire)
        analyse = analyse_questionnaire(questionnaire_traitee)
        reponse = association_definition(analyse)
        
        reponse_associee = association_definition1(reponse)
        reponse_associee2 = association_definition2(reponse)
        
        grande_cat = assoc_grande_categorie(reponse_associee2)
        pagination = mise_en_page(reponse_associee, grande_cat)
        #print(pagination)
        insertion_bilan_premiere_partie(pseudo, pagination)
        


    return render(request, 'le_questionnaire_premiere_partie.html')




from .questionnaire.questionnaire_deux import traitement_DICTEE
from .questionnaire.questionnaire_deux import traitement_texte_utilisateur
from .questionnaire.database.database import insertion_bilan_seconde_partie


from .questionnaire.CONFIG import DICTEE
def le_questionnaire_seconde_partie(request):

    pseudo = request.user

    if request.method == "POST":

        texte = request.POST.get('texte')
        if texte:
            dictee = traitement_DICTEE(DICTEE)
            faute = traitement_texte_utilisateur(texte, dictee)

            if faute == None:
                insertion_bilan_seconde_partie(pseudo, "non")
            else:
                insertion_bilan_seconde_partie(pseudo, faute)
            

    return render(request, 'le_questionnaire_seconde_partie.html')




from .questionnaire.questionnaire_trois import resultat_function
from .questionnaire.questionnaire_trois import correction_questionnaire3
from .questionnaire.database.database import insertion_bilan_troisieme_partie
def le_questionnaire_troisieme_partie(request):

    pseudo = request.user
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
def le_questionnaire_quatrieme_partie(request):

    ok = ""
    pseudo = request.user
    if request.method == "POST":
        resultat = request.POST.get('resultat')

        if resultat:
            result = resultat_function(resultat)
            correct =  correction(result)
            print(correct)
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


        return render(request, 'page_cv.html',
                      {"cv1" : cv[0],
                       "cv2" : cv[1],
                       "cv3" : cv[2],
                       "cv4" : cv[3],
                       "cv5" : cv[4],
                       "cv6" : cv[5],
                       "nom": nom,
                       "prenom": prenom,
                       "addresse": addresse,
                       "fixe": fixe,
                       "portable": portable,
                       "email": email,
                       "form":form}
                      )

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



##    motivation = traitement_motivation(pseudo)
##    mesasge = traitement_message(pseudo)
##                   "motvation1" : motivation[0],
##                   "motvation2" : motivation[1],
##                   "motvation3" : motivation[2],
##                   "motvation4" : motivation[3],
##                   "motvation5" : motivation[4],
##                   "motvation6" : motivation[5],
##                   "message1" : mesasge[0],
##                   "message2" : mesasge[1],
##                   "message3" : mesasge[2],
##                   "message4" : mesasge[3],
##                   "message5" : mesasge[4],
##                   "message6" : mesasge[5],




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
        else:
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

    data = {"nom":nom,
            "prenom":prenom,
            "bilan1":bilan1,
            "bilan2":bilan2,
            "bilan3":bilan3,
            "bilan4":bilan4,
            "pseudo":pseudo,
            "form":form}


    
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
        else:
            pass
 

    if ok is True:
        document_bilan_download(pseudo, "partie_une_bilan_" + str(pseudo) + ".pdf")
        ok = False
    


    data = {"nom":nom,
            "prenom":prenom,
            "bilan1":bilan1,
            "bilan2":bilan2,
            "bilan3":bilan3,
            "bilan4":bilan4,
            "pseudo":pseudo,
            "form":form
            }


    
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
        else:
            pass
 

    if ok is True:
        document_bilan_download(pseudo, "partie_deux_bilan_" + str(pseudo) + ".pdf")
        ok = False
    


    data = {"nom":nom,
            "prenom":prenom,
            "bilan1":bilan1,
            "bilan2":bilan2,
            "bilan3":bilan3,
            "bilan4":bilan4,
            "pseudo":pseudo,
            "form":form
            }


    
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
        else:
            pass
 

    if ok is True:
        document_bilan_download(pseudo, "partie_trois_bilan_" + str(pseudo) + ".pdf")
        ok = False
    


    data = {"nom":nom,
            "prenom":prenom,
            "bilan1":bilan1,
            "bilan2":bilan2,
            "bilan3":bilan3,
            "bilan4":bilan4,
            "pseudo":pseudo,
            "form":form
            }


    
    return render(request, 'page_bilan.html', data)








