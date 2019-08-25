from function_email.recuperation_email import etape_UNE
from function_email.recuperation_email import ETAPE_DEUX
from function_email.recuperation_email import ETAPE_TROIS
from function_email.recuperation_email import ETAPE_QUATTRE
from function_email.recuperation_email import ETAPE_CINQ
from function_email.recuperation_email import ETAPE_SIX
from function_email.recuperation_email import ETAPE_SEPT
from function_email.recuperation_email import ETAPE_HUIT



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



LISTE_INFO.append("lyon")
LISTE_INFO.append("développeur web python")


liste_url_pole = etape_UNE("valence", "développeur web python", "60")
LISTE_LAPINOU.append(liste_url_pole)

liste = ETAPE_DEUX(LISTE_LAPINOU[0])
LISTE_LAPINOU = []
LISTE_LAPINOU.append(liste)



print(len(LISTE_LAPINOU[0]))


Ocontinuer = True
while Ocontinuer:

    if TOUR_BOUCLE == len(LISTE_LAPINOU[0]):

        liste_w = []
        c = 0
        for i in ETAPE_TROIS_LISTE[0]:
            liste_w.append(i)
            if c == 5:
                ETAPE_QUATTRE_LISTE.append(liste_w)
                liste_w = []
                c = 0
            c += 1
            
        ETAPE_QUATTRE_LISTE.append(liste_w)

        Ocontinuer = False
        
        
    else:
        
        liste = ETAPE_TROIS(LISTE_LAPINOU[0][TOUR_BOUCLE],
                            str(LISTE_INFO[1]), str(LISTE_INFO[0]))


        ETAPE_TROIS_LISTE.append(liste[0])
        TOUR_BOUCLE += 1


print(ETAPE_QUATTRE_LISTE[])


























