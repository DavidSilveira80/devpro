from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def portao(request):
    return HttpResponse("Você chegou ao portão da casa")

def sala(request):
    return HttpResponse("Você chegou na sala. senta no sofá!")

def quarto(request):
    return HttpResponse("Agora está no seu quarto, pode se deitar")
