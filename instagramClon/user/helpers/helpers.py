from django.urls import reverse
from django.shortcuts import redirect

def check_login(function):
    def wrapper(*args, **kwargs):
        request = args[1]
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        return function(*args, **kwargs)
    return wrapper
