from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required
def product_list(request):
    return render(request, 'products/product_list.html', {
        'products': Product.objects.all()
    })

@login_required
def product_detail(request, pk):
    return render(request, 'products/product_detail.html', {
        'product': get_object_or_404(Product, pk=pk)
    })

@login_required
def add_product(request):
    if not request.user.profile.is_admin:
        return redirect('product_list')

    if request.method == 'POST':
        Product.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price']
        )
        return redirect('product_list')
    return render(request, 'products/product_form.html')

@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not request.user.profile.is_admin:
        return redirect('product_list')

    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        return redirect('product_list')

    return render(request, 'products/product_form.html', {'product': product})

@login_required
def delete_product(request, pk):
    if request.user.profile.is_admin:
        Product.objects.filter(pk=pk).delete()
    return redirect('product_list')
