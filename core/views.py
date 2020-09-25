from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from . import models
# Create your views here.
def index(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/mensagens")
        else:
            return render(request, "index.html", {})
    elif request.method == "POST":
        user = request.POST.get('user')
        senha = request.POST.get('senha')
        senha_hash = make_password(senha)
        usuario = None
        s = None
        for p in User.objects.raw("SELECT * FROM auth_user WHERE username = '" + user + "'"):
            first = p.password.split('$')[2]
            print(first)
            s = make_password(senha, first)
        
        for p in User.objects.raw("SELECT * FROM auth_user WHERE username = '" + user + "' AND password = '" + s + "'"):
            usuario = p
            print(usuario)
        
        if usuario is not None:
            login(request, usuario)
            return redirect("/mensagens")
        else:
            return render(request, "index.html", {"username": user, "mensagem": "Usuário inválido, tente novamente."})
    else:
        return redirect("/")

@login_required(login_url="/")
def mensagens(request):
    if request.method == "GET":
        men = models.Mensagem.objects.all()
        return render(request, "mensagens.html", {"mensagem": men})
    elif request.method == "POST":
        mensagem = request.POST.get('mensagemescrita')
        models.Mensagem.objects.create(user_id= request.user, mensagem= mensagem)
        return redirect("/mensagens")

@login_required(login_url="/")
def sair(request):
    logout(request)
    return redirect("/")