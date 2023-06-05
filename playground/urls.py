from django.urls import path # for importing url 
from . import views # views.py file

# URLConfig
urlpatterns = [
    path('hello/', views.say_hello)
]