from django.shortcuts import render



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
        
        
    return render(request, 'questionnaire_email.html')


def essais(request):
    return render(request, 'essais.html')
