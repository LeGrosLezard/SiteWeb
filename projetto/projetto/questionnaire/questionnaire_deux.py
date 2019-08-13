

def traitement_DICTEE(DICTEE):
    liste = []
    DICTEE = DICTEE.split()
    for i in DICTEE:
        liste.append(i.lower())

    
    return liste



def traitement_texte_utilisateur(texte, dictee):
    liste = []
    texte = texte.split()

    if len(texte) < 50:
        return None

    else:
        for i in texte:
            liste.append(i.lower())

        try:

            c = 0
            faute = 0
            for i in dictee:
                if i != liste[c]:
                    faute += 1
                c += 1
                
        except IndexError:
            pass


        if faute < 10:
            out = "La personne a moins de 10 erreurs. Elle est ok ect faire le truk pk langage important"

        else:
            out =  None

        return out








        



