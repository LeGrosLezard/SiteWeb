




from .CONFIG import QUESTION
def question_reponse(questionnaire):


    nb = ""
    liste1 = []
    add = False

    for i in questionnaire:
        
        if i == '"':
            add = True
        
        elif i == ",":
            if nb[1] == '"':
                liste1.append(nb[2:-1])
            else:
                liste1.append(nb[1:-1])
            nb = ""

        if add is True and i not in ("[", "]", " "):
            nb += i


    c1 = 0
    liste2 = []
    for i in liste1:
        if c1 % 2 == 0:
            liste2.append([liste1[c1 - 1], liste1[c1]])

        c1 += 1
        
    return liste2







