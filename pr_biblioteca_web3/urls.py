from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse('<body style="margin:0;font-family:sans-serif;background:#1a252f;display:flex;justify-content:center;align-items:center;min-height:100vh;"><div style="background:#fff;padding:40px;border-radius:12px;box-shadow:0 10px 25px rgba(0,0,0,0.15);text-align:center;max-width:500px;width:90%;border-top:5px solid #e74c3c;"><h1 style="color:#2c3e50;margin:0;font-size:2rem;">Página Principal</h1><p style="color:#7f8c8d;margin:15px 0 0 0;font-size:1.1rem;">Bienvenido a la biblioteca.</p></div></body>')),

    path('admin/', admin.site.urls),
    path('catalogo/', include('app_catalogo.urls')),
]