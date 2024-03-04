from django.urls import path
from .views import home, about, chatbot, agency

app_name = "index"

urlpatterns = [
    path("", home, name="home"),
    path("about", about, name="about"),
    path("chatbot", chatbot, name="chatbot"),
    path("agency", agency, name="agency"),
]
