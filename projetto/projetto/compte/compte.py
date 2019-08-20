from .base_de_donnee.info_table import users
def compte_function(pseudo):
    info = users(pseudo)

    return info
