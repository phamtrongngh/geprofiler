import time

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def hello_world(request):
    time.sleep(0.5)
    return HttpResponse("Hello, world!")

@csrf_exempt
def post(request):
    time.sleep(0.5)
    return HttpResponse(request.body, content_type="application/json")
