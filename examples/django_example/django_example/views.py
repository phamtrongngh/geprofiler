import time

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def _get_pets():
    time.sleep(0.5)
    return """
        <ul style="font-size:30px; list-style-type:none;">
            <li>🐱 Cat</li>
            <li>🐶 Dog</li>
            <li>🐯 Lion</li>
            <li>🐰 Rabbit</li>
            <li>🐼 Hamster</li>
            <li>🐻 Bear</li>
            <li>🐨 Koala</li>
        </ul>
        <hr>
        <h2>Add <span style="color: #64cae4" >?geprofiler</span> to url to profile this API.</h2>
    """

def _get_owners():
    time.sleep(0.5)
    return """
        <ul style="font-size:30px; list-style-type:none;">
            <li> 👲 Lee </li>
            <li> 👳 Wayne </li>
            <li> 👵 Tina </li>
            <li> 👶 Jack </li>
        </ul>
        <hr>
        <h2>Add <span style="color: #64cae4" >?geprofiler</span> to url to profile this API.</h2>
    """

def pets(request):
    time.sleep(0.5)
    return HttpResponse(_get_pets())

def owners(request):
    time.sleep(0.5)
    return HttpResponse(_get_owners())
