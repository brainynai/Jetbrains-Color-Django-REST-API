from django.urls import path
from .views import SaturationView, ConvertView, HarmonyView

app_name = "api"

urlpatterns = [
    path('modify-color/', SaturationView.as_view()),
    path('convert-color/', ConvertView.as_view()),
    path('color-harmony/', HarmonyView.as_view()),
]
