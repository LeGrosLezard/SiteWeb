import os
import shutil
import time


from .CONFIG import PATH_FOLDER
from .CONFIG import PATH_FOLDER_CHANGE_NAME
def verification(pseudo, mode):

    
    path = PATH_FOLDER.format(pseudo)
    liste0 = os.listdir(path)
    
    for i in liste0:
        if str(i[:-4]) == mode:
            path1 = PATH_FOLDER_CHANGE_NAME.format(str(pseudo), str(i))
            os.remove(path1)



    
from .CONFIG import PATH_MEDIA_MOTIVATION
from .CONFIG import PATH_MEDIA_MOTIVATION_DOC
from .CONFIG import PATH_FOLDER_CHANGE_NAME
def document_motivation_download(pseudo):

    verification(pseudo, "motivation")

    liste = os.listdir(PATH_MEDIA_MOTIVATION)
    path = PATH_FOLDER.format(pseudo)
    
    for i in liste:
        if str(i[:-4]) == str(pseudo):
            path_doc = PATH_MEDIA_MOTIVATION_DOC.format(i)
            shutil.move(path_doc, path)


    liste1 = os.listdir(path)

    
    for i in liste1:
        if str(i[:-4]) == str(pseudo):

            path2 = PATH_FOLDER_CHANGE_NAME.format(str(pseudo), str(i))
            path3 = PATH_FOLDER_CHANGE_NAME.format(str(pseudo), str("motivation.pdf"))
            os.rename(path2, path3)
    








from .CONFIG import PATH_MEDIA_CV
from .CONFIG import PATH_MEDIA_CV_DOC
from .CONFIG import PATH_FOLDER_CHANGE_NAME
def document_cv_download(pseudo):


    verification(pseudo, "cv")

    liste = os.listdir(PATH_MEDIA_CV)
    path = PATH_FOLDER.format(pseudo)

    
    for i in liste:
        print(i)
        if str(i[:-4]) == str(pseudo):

            path_doc = PATH_MEDIA_CV_DOC.format(i)
            shutil.move(path_doc, path)


    liste1 = os.listdir(path)
    for i in liste1:
        if str(i[:-4]) == str(pseudo):

            path2 = PATH_FOLDER_CHANGE_NAME.format(str(pseudo), str(i))
            path3 = PATH_FOLDER_CHANGE_NAME.format(str(pseudo), str("cv.pdf"))
            os.rename(path2, path3)



from .CONFIG import PATH_MEDIA_MESSAGE
from .CONFIG import PATH_MEDIA_MESSAGE_DOC
from .CONFIG import PATH_FOLDER_CHANGE_NAME
def document_message_download(pseudo):


    verification(pseudo, "message")

    liste = os.listdir(PATH_MEDIA_MESSAGE)
    path = PATH_FOLDER.format(pseudo)

    
    for i in liste:
        if str(i[:-4]) == str(pseudo):

            path_doc = PATH_MEDIA_MESSAGE_DOC.format(i)
            shutil.move(path_doc, path)

    liste1 = os.listdir(path)
    for i in liste1:
        if str(i[:-4]) == str(pseudo):

            path2 = PATH_FOLDER_CHANGE_NAME.format(str(pseudo), str(i))
            path3 = PATH_FOLDER_CHANGE_NAME.format(str(pseudo), str("message.pdf"))
            os.rename(path2, path3)





from .CONFIG import PATH_FOLDER
from .CONFIG import PATH_FOLDER_CHANGE_NAME

def verification_bilan(pseudo, nom_fichier):
    path = PATH_FOLDER.format(pseudo)
    liste0 = os.listdir(path)
    for i in liste0:
        if i == nom_fichier:
            os.remove(PATH_FOLDER_CHANGE_NAME.format(pseudo, i))








from .CONFIG import PATH_MEDIA_BILAN
from .CONFIG import PATH_MEDIA_BILAN_DOC
from .CONFIG import PATH_FOLDER_CHANGE_NAME
def document_bilan_download(pseudo, numero_bilan):

    verification_bilan(pseudo, numero_bilan)
    
    liste0 = os.listdir(PATH_MEDIA_BILAN)

    path = PATH_FOLDER.format(pseudo)

    for i in liste0:
        if i == numero_bilan:
            shutil.move(PATH_MEDIA_BILAN_DOC.format(i), path)




