def traitement_reponse(reponse):

    liste = []

    rep = ""
    for i in reponse:
        for j in i:
            if j == ",":
                liste.append(rep)
                rep = ""
            else:
                rep += j

    return liste
