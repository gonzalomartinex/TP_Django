from django.shortcuts import render
from django.http import HttpResponse
import datetime

def titulo (request):
    doc_externo=open("Documentos/Programacion/Django/proyecto1/supermarket/migrations/index.html")