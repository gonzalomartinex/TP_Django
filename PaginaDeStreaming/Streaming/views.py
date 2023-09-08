from django.shortcuts import render

def frontpage(request):
    return render(request, "frontpage.html")
# Create your views here.
