from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Django')

def detail(request, id):
    return HttpResponse('detail' + str(id))

def create(request):
    return HttpResponse('create')

def update(request, id):
    return HttpResponse('update' + str(id))

def delete(request, id):
    return HttpResponse('delete' + str(id))
