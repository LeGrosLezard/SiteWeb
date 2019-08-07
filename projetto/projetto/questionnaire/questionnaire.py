from .CONFIG import QUESTION
def question_reponse(questionnaire):


    liste = []
    chiffre = ""
    for i in questionnaire:
        if i in ("'", '"', "[", ']', ","):
            pass
        else:


            try:
                i = int(i)
                if i == int(i):
                    chiffre += str(i)
            except:
                liste.append([chiffre, i])
                chiffre = ''


    return liste






