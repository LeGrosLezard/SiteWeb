from django.shortcuts import render


from .function_email.email_function import email
from .function_email.CONFIG import PATH_DOCUMENT
from .function_email.database.database import recup_message
from .function_email.CONFIG import MESSAGE_MAIL
def questionnaire_email(request):

    pseudo = request.user

    if request.method == "POST":

        mail_precis = request.POST.get('mail_precis')
        all_function = request.POST.get('all_function')


        if mail_precis:
            mail1 = request.POST.get('mail1')
            mail2 = request.POST.get('mail2')
            mail3 = request.POST.get('mail3')
            mail4 = request.POST.get('mail4')
            mail5 = request.POST.get('mail5')
            mail6 = request.POST.get('mail6')
            mail7 = request.POST.get('mail7')
            mail8 = request.POST.get('mail8')

            sujet = request.POST.get('sujet')

            liste = [mail1, mail2, mail3, mail4,
                     mail5, mail6, mail7, mail8]

            path_cv = PATH_DOCUMENT.format(pseudo, "cv.pdf")
            path_motivation = PATH_DOCUMENT.format(pseudo, "motivation.pdf")
            msg = recup_message(pseudo)
            message_recruteur = MESSAGE_MAIL.format(msg[0], msg[1], msg[6],
                                                    msg[7], msg[8],
                                                    msg[9], msg[10], msg[11],
                                                    msg[2], msg[3], msg[4], a[5])

            for i in liste:
                if i == "":
                    pass
                else:
                    email(i, sujet, message_recruteur, path_cv, path_motivation)


                
        if all_function:

            metier1 = request.POST.get('metier1')
            metier2 = request.POST.get('metier2')
            metier3 = request.POST.get('metier3')
            metier4 = request.POST.get('metier4')
            metier5 = request.POST.get('metier5')
            metier6 = request.POST.get('metier6')
            metier7 = request.POST.get('metier7')
            ville = request.POST.get('ville')
            rayon = request.POST.get('rayon')

            liste = [metier1, metier2, metier3, metier4,
                     metier5, metier6, metier7]
            
            msg = recup_message(pseudo)
            message_recruteur = MESSAGE_MAIL.format(msg[0], msg[1], msg[6],
                                                    msg[7], msg[8],
                                                    msg[9], msg[10], msg[11],
                                                    msg[2], msg[3], msg[4], a[5])





            

    return render(request, 'questionnaire_email.html')




def essais(request):
    return render(request, 'essais.html')











