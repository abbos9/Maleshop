from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from authentification.forms import SignupForm

from django.views.generic import CreateView, TemplateView
from authentification.models import UserModel
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def SigninView(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("pages:home")
    else:
       return render(request, 'register/signin.html',)
    
    return render(request, 'register/signin.html',)


# def SignupView(request):
#     username = request.POST.get("username")
#     password = request.POST.get("password1")
#     password_confirmed = request.POST.get('password12')
#     if password ==  password_confirmed:
#         user = User.objects.create_user(username=username, password=password)
#         login(request, user)
#         return redirect("pages:home")
#     else:
#         return redirect("authentification:signup")

    
def SignupView(request):
     form = SignupForm()
     if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account has been Created" + user)
            return redirect('authentification:signin')
        else:
            form = UserCreationForm()
        return redirect('authentification:signup')
    
     context = {'form': form}
     return render(request, 'register/signup.html', context=context)
 


def SignoutView(request):
    logout(request)
    return redirect("pages:home")