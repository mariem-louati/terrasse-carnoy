from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()  # ✅ CORRECTION - tous les produits
    return render(request, 'shop/product_list.html', {
        'categories': categories,
        'products': products,  # ✅ CORRECTION - passé au template
    })


def category_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/category_list.html', {
        'categories': categories,
        'products': products,
    })


def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'shop/product_list.html', {
        'products': products,
        'category': category,
        'categories': categories,
    })


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1
    request.session['cart'] = cart
    next_url = request.GET.get('next', 'product_list')
    return redirect(next_url)


def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        product.quantity = quantity
        product.total_price = product.get_display_price() * quantity
        total += product.total_price
        products.append(product)
    return render(request, 'shop/cart.html', {
        'products': products,
        'total': total
    })


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('cart')


def clear_cart(request):
    request.session['cart'] = {}
    return redirect('cart')


def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    request.session['cart'] = cart
    return redirect('cart')


def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})
    pid = str(product_id)
    if pid in cart:
        cart[pid] -= 1
        if cart[pid] <= 0:
            del cart[pid]
    request.session['cart'] = cart
    return redirect('cart')
 
def debug_images(request):
    from django.http import HttpResponse
    from django.conf import settings
    import cloudinary_storage
    import os
    output = f"<p>DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}</p>"
    output += f"<p>CLOUDINARY CLOUD_NAME: {settings.CLOUDINARY_STORAGE.get('CLOUD_NAME', 'NON DEFINI')}</p>"
    output += f"<p>cloudinary_storage version: {cloudinary_storage.__version__}</p>"
    products = Product.objects.all()
    for p in products:
        output += f"<p><b>{p.name}</b> → url: {p.image.url if p.image else 'PAS IMAGE'}</p>"
    return HttpResponse(output)
def migrate_images(request):
    from django.http import HttpResponse
    import cloudinary.uploader
    import os
    from django.conf import settings
    
    output = ""
    products = Product.objects.all()
    
    for p in products:
        if p.image:
            local_path = os.path.join(settings.MEDIA_ROOT, str(p.image))
            if os.path.exists(local_path):
                result = cloudinary.uploader.upload(local_path, folder="products")
                p.image = result['public_id'].replace('products/', '')
                p.save()
                output += f"<p>✅ {p.name} → {result['secure_url']}</p>"
            else:
                output += f"<p>❌ {p.name} → fichier introuvable</p>"
    
    return HttpResponse(output)
 
 