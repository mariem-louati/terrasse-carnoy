from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {
        'categories': categories,
        'products': products,
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
    p = Product.objects.first()
    return HttpResponse(f"image: {p.image} | url: {p.get_image_url()}")


def migrate_images(request):
    from django.http import HttpResponse
    import cloudinary.uploader
    import cloudinary
    import os
    from django.conf import settings

    cloudinary.config(
        cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
        api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
        api_secret=settings.CLOUDINARY_STORAGE['API_SECRET']
    )

    output = ""
    products = Product.objects.all()

    for p in products:
        if p.image:
            image_name = str(p.image).replace('/', os.sep)
            local_path = os.path.join(settings.MEDIA_ROOT, image_name)
            if os.path.exists(local_path):
                result = cloudinary.uploader.upload(local_path, folder="products")
                p.image = result['public_id'].replace('products/', '')
                p.save()
                output += f"<p>✅ {p.name} → {result['secure_url']}</p>"
            else:
                output += f"<p>❌ {p.name} → fichier introuvable</p>"

    return HttpResponse(output)