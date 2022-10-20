
from django.contrib import admin
from django.urls import path, include
from .views import index_generale

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prima_app/',include("prima_app.urls", namespace="prima_app")),
    path('seconda_app/',include("seconda_app.urls", namespace="seconda_app")),
    path('',index_generale, name="index_generale"),
]


