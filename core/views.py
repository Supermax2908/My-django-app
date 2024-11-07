from django.http import HttpResponse
from django.shortcuts import render

from core.tasks import hello_world_task

def hello_world(request):
    name = request.GET.get('name', 'World')

    # Apply async in 3 seconds
    hello_world_task.delay(name)

    return HttpResponse('Hello, World!')


def index(request):
    return render(request, 'index.html')
