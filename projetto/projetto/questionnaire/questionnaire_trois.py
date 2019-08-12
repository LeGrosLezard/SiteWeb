from .CONFIG import questionnaire_3

def resultat_function(resultat):
    
    liste = []
    nb = ""
    for i in resultat:
        if i == ",":
            try:
                liste.append(int(nb))
            except ValueError:
                liste.append(0)
            nb = ""
        else:
            nb += i

    print(liste)


def correction(liste):
    c = 0
    counter = 0
    for i in liste:
        if i == questionnaire_3[c]:
            counter += 1
        c+=1

    return counter
