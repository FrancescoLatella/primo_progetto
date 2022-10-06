from django.urls import path
from prima_app.views import homepage, variabili
app_name="prima_app"
urlpatterns=[
    path('homepage', homepage,name='homepage'),
    path('variabili', variabili,name='variabili'),
]   