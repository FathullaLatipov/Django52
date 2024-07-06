from django.shortcuts import render, redirect

from products.models import ProductModel, CategoryModel


def home_page(request):
    products = ProductModel.objects.all()
    categories = CategoryModel.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'index.html', context=context)

def not_fount_page(request):
    return render(request, 'notfound.html')

def search(request):
    # Пользотватель отправляет Iphone12
    if request.method == 'POST':
        # {'search_product': Iphone12 }
        get_product = request.POST.get('search_product')
        try:
            exact_product = ProductModel.objects.get(product_name__icontains=get_product)
            return redirect(f'/products/{exact_product.id}')
        except:
            return redirect('notfound')

# Страница определенного продукта
def product_page(request, id):
    product = ProductModel.objects.get(id=id)
    context = {'product': product}
    return render(request, 'single-product.html', context=context)


def about_page(request):
    return render(request, 'about.html')
