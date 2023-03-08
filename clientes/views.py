from django.shortcuts import render

def clientes(request):
    context={'clientes':['Donovan','Yoiner','Lili','Daniel']}
    return render(request, 'clientes.html',context)
