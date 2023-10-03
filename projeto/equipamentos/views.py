from django.shortcuts import render, redirect
# from .models import Usuario, ProgramaPosGraduacao
from django.http import HttpResponse

def home(request):
    return HttpResponse("Vamos cadastrar um equipamento")

def cad_equipamento(request):
    return HttpResponse("Vamos cadastrar um equipamento")