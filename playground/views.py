from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# an action

def calculate():
    x = 1
    y = 2
    return x + y

def say_hello(request):
    # pull data from database
    # transform data
    # send email, etc
    # return HttpResponse('Hello World')
    print(calculate())
    return render(request, 'hello.html', {'name': 'Mosh'})
