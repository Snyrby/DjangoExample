from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

'''shows all of the product details
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        # 'title': obj.title,
        # 'description': obj.description,
        # 'price': obj.price
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)
'''


''' renders in a form and saves'''
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        # saves the form
        form.save()
        # re-renders the form
        form = ProductForm()
    context = {
        # 'title': obj.title,
        # 'description': obj.description,
        # 'price': obj.price
        'form': form
    }
    return render(request, 'products/product_create.html', context)


''' This will retrieve data from the form so it can be used for processing, etc.
def product_create_view(request):
    if request.method == 'POST':
        my_new_title = request.POST.get('title')
        # Product.objects.create(title=my_new_title)
        print(my_new_title)
    context = {}
    return render(request, 'products/product_create.html', context)
'''

'''form for raw data and converting
def product_create_view(request):
    form = RawProductForm()
    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            # now the data is good
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'products/product_create.html', context)'''

''' this goes over pulling database info into formdata and editing
def product_create_view(request):
    initial_data = {'title': 'My this awesome title'}
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    # instance will pass in database object
    # initial=initial_data to provide initial data
    context = {'form': form}
    return render(request, 'products/product_create.html', context)'''

'''dynamic url routing'''
def product_detail_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    '''
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    '''
    context = {'object': obj}
    return render(request, 'products/product_detail.html', context)

# in order to handle a missing object from a dynamic url import get_object_or_404 shortcut

def product_delete_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        # to delete objects you just. This comes from get request though:
        # now in if statement it is confirming
        obj.delete()
        return redirect('../../')
    context = {'object': obj}
    return render(request, 'products/product_delete.html', context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {'object_list': queryset}
    return render(request, 'products/product_list.html', context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        # instance will pass in database object
        # initial=initial_data to provide initial data
    context = {'form': form}
    return render(request, 'products/product_create.html', context)