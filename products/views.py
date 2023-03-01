from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        # 'title': obj.title,
        # 'description': obj.description,
        # 'price': obj.price
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)


''' renders in a form and saves '''
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