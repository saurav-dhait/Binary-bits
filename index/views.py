from django.shortcuts import HttpResponse, get_object_or_404, render
from django.http import JsonResponse
from .models import Agency


def home(request):
    return render(request, "index/home.html")


def about(request):
    return render(request, "index/about.html")


def chatbot(request):
    return render(request, "index/chatbot.html")


def get_agency_details(request, agency_id):
    agency = get_object_or_404(Agency, id=agency_id)
    data = {
        "id": agency.id,
        "address": agency.address,
        "type_of_agency": agency.type_of_agency,
        "contact": agency.contact,
        "email": agency.email,
    }
    context = {"data":data}
    return render(request, "index/agency.html", context=context)
