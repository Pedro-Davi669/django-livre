from django.urls import path
from loja.Views.HomeView import home_view
urlpatterns = [
    path("", home_view),
]