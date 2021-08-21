from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def galerie(request):
    return render(request, "galerie.html")

def entreprise(request):
    return render(request, "entreprise.html")