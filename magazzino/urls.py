from django.contrib import admin
from django.urls import path,include
from .views import MagazzinoList


urlpatterns = [
        path('list', MagazzinoList.as_view()),     
]