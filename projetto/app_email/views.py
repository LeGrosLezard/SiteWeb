from django.shortcuts import render
from django.http import HttpResponse


#Here it's for no automatic email
from .views_function import mail_precis_function

#Here we traiting data send by uder(job, localisation)
from .views_function import traitement_reponse

from .function_email.recuperation_email import etape_UNE
from .function_email.recuperation_email import ETAPE_DEUX
from .function_email.recuperation_email import ETAPE_TROIS
from .function_email.recuperation_email import ETAPE_QUATTRE
from .function_email.recuperation_email import ETAPE_CINQ
from .function_email.recuperation_email import ETAPE_SIX
from .function_email.recuperation_email import ETAPE_SEPT
from .function_email.recuperation_email import ETAPE_HUIT

LISTE_INFO = []
LISTE_LAPINOU = []
TOUR_BOUCLE = 0
ETAPE_TROIS_LISTE = []
ETAPE_QUATTRE_LISTE = []
ETAPE_CINQ_LISTE = []
EMAILS = []
TOUR_BOUCLE_TROIS = 0
TOUR_BOUCLE_CINQ = 0
ETAPE_SIX_LISTE = []
ETAPE_SIX_LISTE_JE_ME_PERDS = []
ENTREPRISE = []
ETAPE_SIX_DERNIERE_LISTE = []

def questionnaire_email(request):

    global LISTE_LAPINOU
    global LISTE_INFO
    global TOUR_BOUCLE
    global ETAPE_TROIS_LISTE
    global ETAPE_QUATTRE_LISTE
    global EMAILS
    global ETAPE_CINQ_LISTE
    global TOUR_BOUCLE_TROIS
    global TOUR_BOUCLE_CINQ
    global ETAPE_SIX_LISTE
    global ENTREPRISE
    global ETAPE_SIX_DERNIERE_LISTE

    
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
            #We insert this information for later
            LISTE_INFO.append(emploi)
            LISTE_INFO.append(lieu)
            #let's do the first search !!!
            liste_url_pole = etape_UNE(lieu, emploi, "60")
            LISTE_LAPINOU.append(liste_url_pole)
            return HttpResponse("ok")
        
        if un:#ETAPE 2
            liste = ETAPE_DEUX(LISTE_LAPINOU[0])
            LISTE_LAPINOU = []
            LISTE_LAPINOU.append(liste)
            return HttpResponse("ok")

        if deux:#ETAPE 3

            if TOUR_BOUCLE == len(LISTE_LAPINOU[0]):
                
                liste_w = []
                c = 0
                for i in ETAPE_TROIS_LISTE[0]:
                    liste_w.append(i)
                    if c == 20:
                        ETAPE_QUATTRE_LISTE.append(liste_w)
                        liste_w = []
                        c = 0
                    c += 1
                ETAPE_QUATTRE_LISTE.append(liste_w)

                return HttpResponse("fini")
            
            else:
                try:
                    liste = ETAPE_TROIS(LISTE_LAPINOU[0][TOUR_BOUCLE],
                                        str(LISTE_INFO[1]), str(LISTE_INFO[0]))

                    ETAPE_TROIS_LISTE.append(liste[0])
                    TOUR_BOUCLE += 1
                    return HttpResponse("ok")
                except:
                    liste_w = []
                    c = 0
                    for i in ETAPE_TROIS_LISTE[0]:
                        liste_w.append(i)
                        if c == 20:
                            ETAPE_QUATTRE_LISTE.append(liste_w)
                            liste_w = []
                            c = 0
                        c += 1
                    ETAPE_QUATTRE_LISTE.append(liste_w)

                    return HttpResponse("fini")
        
        if trois:#ETAPE 4
            liste_w = []
            
            if TOUR_BOUCLE_TROIS == len(ETAPE_TROIS_LISTE):
                c = 0
                for i in ETAPE_QUATTRE_LISTE[0]:
                    liste_w.append(i)
                    if c == 5:
                        ETAPE_CINQ_LISTE.append(liste_w)
                        liste_w = []
                        c = 0
                    c+=1
                ETAPE_CINQ_LISTE.append(liste_w)
                
                return HttpResponse("fini")
 
            else:
                email, liste = ETAPE_QUATTRE(ETAPE_TROIS_LISTE[TOUR_BOUCLE_TROIS])
                ETAPE_QUATTRE_LISTE.append(liste)
                EMAILS.append(email)
                TOUR_BOUCLE_TROIS += 1

                return HttpResponse("ok")


        if quattre:#ETAPE 5
            liste_w = []
            if len(ETAPE_CINQ_LISTE) == TOUR_BOUCLE_CINQ:

                c = 0

                for i in ETAPE_SIX_LISTE:
                    liste_w.append(i)
                    if c == 20:
                        ETAPE_SIX_LISTE_JE_ME_PERDS.append(liste_w)
                        liste_w = []
                        c = 0
                    c += 1
                ETAPE_SIX_LISTE_JE_ME_PERDS.append(liste_w)
                return HttpResponse("fini")

            else:
                liste, liste_no = ETAPE_CINQ(ETAPE_CINQ_LISTE[TOUR_BOUCLE_CINQ])

                ENTREPRISE.append(liste)
                ETAPE_SIX_LISTE.append(liste_no)
                TOUR_BOUCLE_CINQ += 1
                return HttpResponse("ok")

            
        
        if cinq:#ETAPE 6
            ETAPE_SIX_DERNIERE_LISTE = ETAPE_SIX(ETAPE_SIX_LISTE_JE_ME_PERDS)
            print(ETAPE_SIX_DERNIERE_LISTE)
            return HttpResponse("fini")

        
        if six:
            ENTREPRISE = ETAPE_SEPT(ETAPE_SIX_DERNIERE_LISTE)
            print(ENTREPRISE)
            return HttpResponse("fini")
        if sept:
            mail = ETAPE_HUIT(ENTREPRISE, LISTE_INFO[1])
            EMAILS.append(mail)

            print(EMAILS)





    return render(request, 'questionnaire_email.html')




def essais(request):
    return render(request, 'essais.html')











