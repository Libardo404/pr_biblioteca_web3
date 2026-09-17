from django.http import HttpResponse

def inicio(request):
    return HttpResponse('<body style="margin:0;font-family:sans-serif;background:#f4f7f6;display:flex;justify-content:center;align-items:center;min-height:100vh;"><div style="background:#fff;padding:40px;border-radius:12px;box-shadow:0 4px 15px rgba(0,0,0,0.05);text-align:center;max-width:500px;width:90%;border-top:5px solid #2c3e50;"><h1 style="color:#2c3e50;margin:0;font-size:2rem;">¡Bienvenido!</h1><p style="color:#7f8c8d;margin:15px 0 0 0;font-size:1.1rem;">Al catálogo de la biblioteca</p></div></body>')