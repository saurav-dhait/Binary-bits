from django.urls import path
from .views import get_agency_details, home, about, chatbot

app_name = "index"

urlpatterns = [
    path("", home, name="home"),
    path("about", about, name="about"),
    path("chatbot", chatbot, name="chatbot"),
    path("agency/<uuid:agency_id>", get_agency_details, name="agency"),
]
