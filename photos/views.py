from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse('안녕하세요!')

def detail(request, pk):
    msg = '{}번 사진 보여줄게요.'.format(pk)
    return HttpResponse(msg)