import os

from .CONFIG import PATH_FOLDER

def verify_document_cv(pseudo):
    """Here we chec if cv is already present"""

    path = PATH_FOLDER.format(pseudo)

    liste = os.listdir(path)

    for i in liste:
        if i == "cv.pdf":
            emplacement = str(pseudo) + "\cv.pdf"
            suppression(PATH_FOLDER.format(emplacement))
    


def suppression(i):
    os.remove(i)





























