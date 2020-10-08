import json
from inspect import v

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view


def hello(request):
    return HttpResponse('hello world!')


@api_view(['POST'])
def bugs(request):
    source = {"business_autoFans_J": [14, 15, 9],
              "autoAX": [7, 32, 0],
              "autoAX_admin": [5, 13, 2]}

    total = 0
    name = request.POST.get('name')
    if name is not None:
        return JsonResponse(data={"total": sum(source(name)), "name": name})
    else:
        AllBugs = 0

        for i in source.values():
            AllBugs += sum(i)
        return JsonResponse(data={"total": AllBugs, "name": 'all'})
