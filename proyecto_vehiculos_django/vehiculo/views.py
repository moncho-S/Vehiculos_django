from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import *

# Create your views here.
def inicioView(request):
    context={}
    return render(request,'index.html',context)

@csrf_protect
def addView(request):
    context={}
    form=VehiculoForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        #newvalor=form.cleaned_data['valoracion']#toma valor valoracion 
        form.save()
        return HttpResponseRedirect('../')
    context={
        'form':form,
        }
    return render(request,'add.html',context)

def listView(request):
    data=VehiculoModel.objects.all()
    for d in data:
        if d.precio>30000:
            d.validacion='Alto'
        elif d.precio>10000:
            d.validacion='Medio'
        else:
            d.validacion='Bajo'
    context={'data':data}
    return render(request,'listado.html',context)


def logoutView(request):
    logout(request)
    messages.info(request,"se ha cerrado la sesion")
    return HttpResponseRedirect("../")

def vehiculoView(request):
    return HttpResponseRedirect("../")

def loginView(request):
    if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f'valido como {username}')
                return HttpResponseRedirect("../")
            else:
                messages.error(request,'invalido')
        else:
            messages.error(request,'invalido')
    form=AuthenticationForm()
    context={
        "login_form":form
    }
    return render(request,'login.html',context)