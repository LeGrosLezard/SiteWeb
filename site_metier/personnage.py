class Personnage:

    def __init__(self, nom, age, sexe, city):

        self.nom = nom
        self.age = age
        self.sexe = sexe
        self.city = city
        



class Capacite:

    def __init__(self, passion, ancien_job_le_plus_plaisant,
                 serie, film):

        self.passion = passion
        self.ancien_job_le_plus_plaisant = ancien_job_le_plus_plaisant
        self.serie = serie
        self.film = film

        

    def function(passion, ancien_job_le_plus_plaisant,
                 serie, film):

        if passion == "":
            pass
        elif passion == "":
            pass




class Comportement:
    
    def __init__(self, file_attente, anniversaire, soirée, cinema,
                 volant, barre, enterrement):

        self.file_attente = file_attente
        self.anniversaire = anniversaire
        self.soirée = soirée
        self.cinema = cinema
        self.volant = volant
        self.barre = barre
        self.enterrement = enterrement
        



class Musique:

    def __init__(self, metal, rap, pop, culture,
                 classique, club, boomboom):

        self.metal = metal
        self.rap = rap
        self.pop = pop
        self.culture = culture
        self.classique = classique
        self.club = club
        self.boomboom = boomboom


class Apparence:
    
    def __init__(self, bien_sur_soi, negligé, coupe, habits_haut,
                 habits_bas, couleur_la_plus_presente, muscle,
                 maigre, gros, obeze, ongle, bouton):

        self.bien_sur_soi = bien_sur_soi
        self.negligé = negligé
        self.coupe = coupe
        self.habits_haut = habits_haut
        self.habits_bas = habits_bas
        self.couleur_la_plus_presente = couleur_la_plus_presente
        self.muscle = muscle
        self.maigre = maigre
        self.gros = gros
        self.obeze = obeze
        self.ongle = ongle
        self.bouton = bouton


    def ongle_(ongle):

        if ongle =="":
            pass



if __name__ == "__main__":

    bogoss = Personnage("jb", "25", "H", "Aouste", "50", "50","50")
    habit_du_bogoss = Habit("torse poil", "jogging", "patte", "écouteur", "type casque")

    print(habit_du_bogoss.couleur_cheveux)

    a = Habit.function(habit_du_bogoss.couleur_cheveux)































        
