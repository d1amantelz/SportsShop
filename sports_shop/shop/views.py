from django.shortcuts import render, redirect

from shop.forms import EditProductForm
from shop.models import *

title = 'SShop - интернет магазин спортивных товаров'


def index(request):
    products = Products.objects.all()
    categories = Categories.objects.all()

    context = {
        'products': products,
        'title': title,
        'cats': categories,
        'cat_selected': 0,
    }
    return render(request, 'shop/index.html', context=context)


def change_product(request, product_id):
    categories = Categories.objects.all()
    product = Products.objects.get(pk=product_id)

    if request.method == 'POST':
        form = EditProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditProductForm(instance=product)

    context = {
        'product': product,
        'cats': categories,
        'form': form,
        'title': 'Изменения товара',
        'cat_selected': product.category_id,
    }
    return render(request, 'shop/change_product.html', context=context)


def show_category(request, cat_id):
    products = Products.objects.filter(category_id=cat_id)
    categories = Categories.objects.all()

    context = {
        'products': products,
        'cats': categories,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id}

    return render(request, 'shop/index.html', context=context)
