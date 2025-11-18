from django.shortcuts import render,  get_object_or_404, redirect
from django.http import HttpResponse

def post_list(request):
   return render(request, 'blog/post_list.html', {})

def portao(request):
    return HttpResponse('Você chegou ao portão da casa!')

def sala(request):
    return HttpResponse("Você chegou na sala. Senta no sofá!")

def quarto(request):
    return HttpResponse("Agora está no quarto, pode se deitar!")