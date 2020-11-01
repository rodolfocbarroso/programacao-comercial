from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render

class Autenticacao(View):

    def get(self, request):
        contexto = {
            'usuario': 'teste',
            'senha': '12345'
            }
        return render(request, 'autenticacao.html', contexto)