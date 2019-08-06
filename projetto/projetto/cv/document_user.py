import os
import shutil
import time


from .CONFIG import PATH_FOLDER


def verification(pseudo, mode):

    
    path = PATH_FOLDER.format(pseudo)
    
    liste0 = os.listdir(path)
    for i in liste0:
        if i[:-4] == mode:
            os.remove(i)



    
from .CONFIG import PATH_MEDIA_MOTIVATION
from .CONFIG import PATH_MEDIA_MOTIVATION_DOC
def document_motivation_download(pseudo):

    
    verification(pseudo, "motivation")

    liste = os.listdir(PATH_MEDIA_MOTIVATION)
    path = PATH_FOLDER.format(pseudo)

    
    for i in liste:
        if i[:-4] == pseudo:

            path_doc = PATH_MEDIA_MOTIVATION_DOC.format(i)
            shutil.move(path_doc, path)


    liste1 = os.listdir(path)
    for i in liste1:
        if i[:-4] == pseudo:
            os.rename(i, "motivation.pdf")
    








from .CONFIG import PATH_MEDIA_CV
from .CONFIG import PATH_MEDIA_CV_DOC
def document_cv_download(pseudo):


    verification(pseudo, "cv")

    liste = os.listdir(PATH_MEDIA_CV)
    path = PATH_FOLDER.format(pseudo)

    
    for i in liste:
        if i[:-4] == pseudo:

            path_doc = PATH_MEDIA_CV_DOC.format(i)
            shutil.move(path_doc, path)


    liste1 = os.listdir(path)
    for i in liste1:
        if i[:-4] == pseudo:
            os.rename(i, "cv.pdf")



from .CONFIG import PATH_MEDIA_MESSAGE
from .CONFIG import PATH_MEDIA_MESSAGE_DOC
def document_message_download(pseudo):


    verification(pseudo, "message")

    liste = os.listdir(PATH_MEDIA_MESSAGE)
    path = PATH_FOLDER.format(pseudo)

    
    for i in liste:
        if i[:-4] == pseudo:

            path_doc = PATH_MEDIA_MESSAGE_DOC.format(i)
            shutil.move(path_doc, path)

    liste1 = os.listdir(path)
    for i in liste1:
        if i[:-4] == pseudo:
            os.rename(i, "message.pdf")


from .CONFIG import PATH_MEDIA_BILAN
from .CONFIG import PATH_MEDIA_BILAN_DOC
def document_bilan_download(pseudo):


    verification(pseudo, "bilan")

    liste = os.listdir(PATH_MEDIA_BILAN)
    path = PATH_FOLDER.format(pseudo)

    
    for i in liste:
        if i[:-4] == pseudo:

            path_doc = PATH_MEDIA_BILAN_DOC.format(i)
            shutil.move(path_doc, path)

    liste1 = os.listdir(path)
    for i in liste1:
        if i[:-4] == pseudo:
            os.rename(i, "bilan.pdf")




