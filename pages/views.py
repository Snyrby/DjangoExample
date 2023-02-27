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
    my_context = {'my_text': 'This is about us', 'my_number': 123,  'my_list': [123, 4242, 12313]}
    return render(request, 'contact.html', my_context)
