import os

from .CONFIG import PATH_FOLDER

def verify_document_cv(pseudo, doc):
    """Here we chec if cv is already present"""

    path = PATH_FOLDER.format(pseudo)

    liste = os.listdir(path)

    for i in liste:
        if i[:4] == str(doc):
            return "verification"

            
    return None
































