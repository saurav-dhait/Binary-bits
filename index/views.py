from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "index/home.html")


def about(request):
    return render(request, "index/about.html")


def chatbot(request):
    return render(request, "index/chatbot.html")


def agency(request):
    return render(request, "index/agency.html")
