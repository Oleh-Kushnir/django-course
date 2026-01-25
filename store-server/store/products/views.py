from django.shortcuts import render

from products.models import Products,ProductCategory
# Create your views here.

def index(request):
    context = {
        'is_promotion': False
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'products': Products.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)