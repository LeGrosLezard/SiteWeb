"""projetto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('compte', views.compte),
    path('questionnaire', views.questionnaire),
    path('comment_faire_mon_cv', views.comment_faire_mon_cv),
    path('ma_demarche', views.ma_demarche),
    path('le_questionnaire', views.le_questionnaire),
    path('le_questionnaire_premiere_partie', views.le_questionnaire_premiere_partie),
    path('le_questionnaire_seconde_partie', views.le_questionnaire_seconde_partie),
    path('le_questionnaire_troisieme_partie', views.le_questionnaire_troisieme_partie),
    path('le_questionnaire_quatrieme_partie', views.le_questionnaire_quatrieme_partie),
    path('mon_cv', views.mon_cv),
    path('ma_lettre', views.ma_lettre),
    path('mon_message', views.mon_message),
]

































