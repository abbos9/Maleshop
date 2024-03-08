from django.urls import path
from authentification.views import SigninView, SignupView,  SignoutView
from django.contrib.auth import  views as auth_views

app_name = 'authentification'

urlpatterns = [
    path('signin/', SigninView, name='signin'),
    path('signup/', SignupView, name='signup'),
    path("signout/", SignoutView, name = 'signout'),
    # path("login/", auth_views.LoginView.as_view(), name='login'),
]