from .base_de_donnee.remplissage_user import insertion_user



def inscription(pseudo, nom, prenom, date, sexe, email,
                portable, fixe, adresse, password):
    
    insertion_user(nom, prenom, date, sexe, email,
                    fixe, password, pseudo, adresse,
                    portable)



