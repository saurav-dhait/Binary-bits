from django.urls import path
from .views import report_home,map_display

app_name = "report"

urlpatterns = [
    path("", report_home, name="home"),
    path("map_display", map_display, name="map_display"),
]
