from .forms import *
from user.models import User
from django.views import View
from django.urls import reverse
from django.contrib import messages
from .helpers.helpers import check_login
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .service.user_service import UserService
from django.contrib.auth import authenticate,login, logout

# Mi flujo es <Controlador> <-> <Servicio> <-> <Repositorio> <-> <Modelo>
# Elijo que siempre a servicio por si cambia un poco la logica de algo (registro por ejemplo), el repositorio no hace falta tocarlo.

class SignUpView(View):
    def __init__(self):
        self._user_service = UserService()

    @check_login
    def get(self,request):
        return render(request, 'signup.html', {'form': SignUpForm()})

    def post(self,request):
        # print(request.data)
        form = SignUpForm(request.POST)
        if form.is_valid():
            self._user_service.register_user(form.cleaned_data)
            return redirect(reverse('user:login'))
        return render(request, 'signup.html', {'form': form})

class LoginView(View):
    @check_login
    def get(self,request):
        return render(request, 'login.html', {'form': LoginForm()})

    @csrf_exempt
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password']) 
            if user is not None:
                login(request,user)
                messages.add_message(request, messages.SUCCESS, 'Login Sucessfull.')
                return redirect(reverse('home'))
        
        messages.add_message(request, messages.ERROR, 'Invalid Data.')
        return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect(reverse('user:login'))

