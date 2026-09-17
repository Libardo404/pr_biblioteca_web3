from django.urls import path
from django.urls import path
from . import views

app_name = 'catalogo'  # namespace, útil para {% url %}

urlpatterns = [
    path('', views.inicio, name='inicio'),
]