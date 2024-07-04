from django.shortcuts import render

from products.models import ProductModel, CategoryModel


def home_page(request):
    products = ProductModel.objects.all()
    categories = CategoryModel.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'index.html', context=context)


def about_page(request):
    return render(request, 'about.html')
