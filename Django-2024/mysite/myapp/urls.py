from django.urls import path
from . import views

# define the list of url patterns

urlpatterns = [
    path('', views.index)
]