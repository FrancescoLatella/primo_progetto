from django.shortcuts import render
import datetime
# Create your views here.

def es_if(request):
    context = {
        'var1' : 200,
        'var2' : 200,
        'var3' : 300
         
    }
    return render(request, "es_if.html", context)

def if_else_elif(request):
    context = {
        'var1' : 100,
        'var2' : 100.0,
        'var3' : 100.50,
    }
    
    return render(request, "if_else_elif.html", context)

def es_for(request):
    context = {
        'lista1' : [1, datetime.date(2019,7,16), 'Do not give up!'],
        'lista2' : [1, datetime.date(2019,7,16), 'Do not give up!']
    }

    return render(request, "es_for.html", context)

def index2(request):
    return render(request, "index2.html")

def view_a(request):
    return render(request, "view_a.html")

def view_b(request):
    return render(request, "view_b.html")

def view_c(request):
    return render(request, "view_c.html")


