from django.shortcuts import render
from requests import request
from .models import Product
from .forms import ProductForm


# Create your views here.
def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    '''context = {
        'title': obj.title,
        'description': obj.description
    }'''
    context = {
        'object': obj
    }
    return render(request, "product/detail.html", context)




def product_create_view(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "product/create.html", context)