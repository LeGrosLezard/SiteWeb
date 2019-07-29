from django.shortcuts import render



def questionnaire_email(request):
    return render(request, 'questionnaire_email.html')

