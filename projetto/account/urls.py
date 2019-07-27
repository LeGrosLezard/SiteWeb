from django.urls import path

from . import views


urlpatterns = [
    path(r'register/', views.register),
    path(r'login/', views.login_view),

]
