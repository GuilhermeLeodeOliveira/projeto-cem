from django.shortcuts import render, redirect
#from .models import 
from django.http import HttpResponse
# Create your views here.
def login_adm(request):
    return render(request, 'login_adm.html')