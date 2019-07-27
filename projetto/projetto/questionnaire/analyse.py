from .CONFIG import Ouverture_a_l_experience
from .CONFIG import Conscience_professionnelle
from .CONFIG import Extraversion
from .CONFIG import Agreabilite
from .CONFIG import Reactions_naturelles





#TOLERENCE A LA DIVERSITEEE PROBLEEME (les haut score sont grave défiant de loto)
#ANXIETE AUSSI (score bas == cool)
#Colère et hostilité
#Morosité/contentement:
#Indolencen, Sensibilité, Affectation


from .CONFIG import QUESTION
def analyse_questionnaire(questionnaire):

    SOUS_CAT = {
        "Imagination": 0,
        "Interets_artistiques": 0,
        "Profondeur_des_emotions" : 0,
        "Volonte_experimenter" : 0,
        "Curiosite_intellectuelle" : 0,
        "Tolerance_a_la_diversite" : 0,
        "Sens_des_competences" : 0,
        "Ordre" : 0,
        "Sens_des_responsabilites" : 0,
        "Combativite_Recherche_de_resultats" : 0,
        "Autodiscipline" : 0,
        "Circonspection" : 0,
        "Amenite" : 0,
        "Sociabilite" : 0,
        "Assertivite" : 0,
        "Niveau_d_activite" : 0,
        "Recherche_de_stimulation" : 0,
        "emotions_positives" : 0,
        "Confiance_en_autre"  : 0,
        "Sincerite" : 0,
        "Altruisme" : 0,
        "Conformite" : 0,
        "Modestie" : 0,
        "Sympathie" : 0,
        "Anxiete"  : 0,
        "Colere_et_hostilite" : 0,
        "Morosite_contentement"  : 0,
        "Affectation" : 0,
        "Indolence" : 0,
        "Sensibilite_au_stress" : 0,
        }

    dico_pts = {"a": 1, "b": 0.5, "c": 0, "d": -0.5, "e": -1}

 
    for i in questionnaire:
        #On parcours la liste nettoyé

        for cle, valeur in QUESTION.items():
            #On parcours la liste de question associé a la classe
            #de personnalité

            if cle == i[0]:
                #on comapre le numéro de la question avec le numéro de la
                #le type a répondu a la 52 -> la 52 = Ordre

                for cle1, valeur1 in SOUS_CAT.items():
                    if valeur == cle1:
                        #Mtn on va scoriser
                        #Du genre on cherche Ordre (global variable)
                    
                        for cle2, valeur2 in dico_pts.items():
                            if i[1] == cle2:
                                #on a la réponse sous forme a,b,c,d,e
                                #ou a = 1 et e = -1
                                
                                SOUS_CAT[cle1] += int(valeur2)
                                #On l'ajoute au dico
        


                    elif valeur[1:] == cle1:
                        #Sinon si la phrase est tournée du genre
                        #Je n'aime pas la poesie
                        #Conteste curiosité art
                        #si le mec dit oui tout a fait dac
                        #on met -1 a ce truk
                        #par contre s'il dit non pas du tout
                        #a la base c du -1 donc ca devient du + 1 pour art
                        for cle2, valeur2 in dico_pts.items():
                            if i[1] == cle2:
                                #on a la réponse sous forme a,b,c,d,e
                                #ou a = 1 et e = -1
                                
                                SOUS_CAT[cle1] -= int(valeur2)
                                #On l'ajoute au dico

    return SOUS_CAT

def association_definition(dico):

    liste_supp = []
    liste_inf = []



    for cle, valeur in dico.items():
        if valeur > 0:
            liste_supp.append(cle)
        elif valeur < 0:
            liste_inf.append(cle)



    return liste_supp, liste_inf


from .CONFIG import SOUS_CLASSE
def association_definition1(liste_supp, liste_inf):
    
    liste_qualite = []
    liste_a_w = []
    
    for i in liste_supp:
        for cle, valeur in SOUS_CLASSE.items():
            if cle == i:
                liste_qualite.append(valeur)



    for i in liste_inf:
        for cle, valeur in SOUS_CLASSE.items():
            if cle == i:
                liste_a_w.append(valeur)


    print(liste_qualite, liste_a_w)
    return liste_qualite, liste_a_w

























