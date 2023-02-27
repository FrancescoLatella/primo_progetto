from django.urls import path
from prova_pratica_2.views import view_lista_targhe, view_b
app_name="prova_pratica_2"
urlpatterns=[
    path("view_lista_targhe/",view_lista_targhe,name="view_lista_targhe"),
    path("view_b/",view_b,name="view_b"),
]