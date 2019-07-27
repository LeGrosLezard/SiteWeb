

from .database import recuperation_nom
from .database import recuperation_bilan
from .database import recuperation_motivation

def recuperation_info(pseudo):
    """On recupere les informations nécéssaire
    au cv"""

    
    nom, prenom = recuperation_nom(pseudo)
    bilan = recuperation_bilan(pseudo)
    motivation recuperation_motivation(pseudo)

    return nom, prenom, bilan, motivation
