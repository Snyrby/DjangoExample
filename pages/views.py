from django.http import HttpResponse
from django.shortcuts import render

# request -> response
# request handler
# an action
# Create your views here.

def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})
