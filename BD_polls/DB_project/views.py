from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
# from django.template.context import RequestContext


def login(request):
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/')