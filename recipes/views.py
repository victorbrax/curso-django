from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('HOME 1')

def contato(request):
    return HttpResponse('contato')
