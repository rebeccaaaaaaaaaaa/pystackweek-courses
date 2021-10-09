from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario


def cadastro(request):
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    #VERIFICAR SE O EMAIL DO USUARIO JA EXISTE
    usuario = Usuario.objects.filter(email = email)

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=1')
    
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=2')
    
    if len(senha) < 8 or len(senha) > 12:
        return redirect('/auth/cadastro/?status=3')
    
    try:
        senha = hashlib.sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome,
                          email = email,
                          senha = senha)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')