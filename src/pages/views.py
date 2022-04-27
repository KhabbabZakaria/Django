from django.shortcuts import render
from django.http import HttpResponse
from requests import request

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    my_context = {
        "my_text": "Welcome Developers!!!",
        "my_number": 7,
        "my_list": [1,2,3]
    }
    return render(request, "home.html", my_context)