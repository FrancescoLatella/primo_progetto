from django.shortcuts import render

# Create your views here.

def view_a(request):
    lista_materie=[]
    lista_materie.append("Matematica")
    lista_materie.append("Italiano")
    lista_materie.append("Inglese")
    lista_materie.append("Storia")
    lista_materie.append("Geografia")
    context={
        'var1':lista_materie,
    }
    return render(request, "view_a.html",context)

def view_b(request):
    studenti={'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    context={
        'var2':studenti,
    }
    return render(request, "view_b.html",context)

def view_c(request):
    dati=studenti["Nicola Spina"]
    print(dati)
    media=0

    for dato in dati:
        media+=dato[1]
        media=media/len(dati)
        print("Media="+str(media))
        return render(request, "view_c.html")
