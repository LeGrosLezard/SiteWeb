from .CONFIG import questionnaire_3

def resultat_function(resultat):

    liste = []
    nb = ""
    for i in resultat:

        if i == ",":
            try:
                liste.append(int(nb))
                nb = ""
            except ValueError:
                liste.append(0)
            
        else:
            nb += i

    return liste

def correction_questionnaire3(liste):

    c = 0
    counter = 0

    for i in liste:

        if int(i[0]) == questionnaire_3[c]:
            counter += 1
        c+=1

    return counter



