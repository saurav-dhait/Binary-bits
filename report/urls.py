from django.urls import path
from .views import report_home

app_name = "report"

urlpatterns = [
    path("", report_home, name="home"),
]
