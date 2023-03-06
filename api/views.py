from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
import json
from .models import Person
from django.contrib.auth.models import User
from .models import Person
# Create your views here.


def get_users(request: HttpRequest, pk: int):

    users = Person.objects.get(id=pk)
    return JsonResponse({
        'id':users.id,
        'username':users.first_name,
        'password':users.last_name
    })

def add_user(request: HttpRequest):
    body = request.body.decode()
    data = json.loads(body)

    p = Person(
        first_name = data['first_name'],
        last_name = data['last_name']
    )
    p.save()
    return JsonResponse({'ok':200})

