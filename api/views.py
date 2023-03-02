from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
# Create your views here.


def home(request: HttpRequest):

    data = request.GET

    a = int(data.get('a',0))
    b = int(data.get('b',0))

    
    return JsonResponse({
        'sum':a+b
    })

