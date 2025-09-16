from django.shortcuts import render
from store.models import Category, Product  # adjust if your models are in a different app
from django.shortcuts import render, get_object_or_404

def index(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'ecom-template/index.html', context)



def store(request):
    # Get category slug from URL query parameter
    category_slug = request.GET.get('category')
    products = Product.objects.filter(is_available=True)

    if category_slug:
        products = products.filter(category__slug=category_slug)

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'selected_category': category_slug,
    }
    return render(request, 'ecom-template/store.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    categories = Category.objects.all()
    context = {
        'product': product,
        'categories': categories,
    }
    return render(request, 'ecom-template/product-detail.html', context)

def cart(request):
    return render(request, 'ecom-template/cart.html')

def place_order(request):
    return render(request, 'ecom-template/place-order.html')

def order_complete(request):
    return render(request, 'ecom-template/order_complete.html')

def dashboard(request):
    return render(request, 'ecom-template/dashboard.html')

def register(request):
    return render(request, 'ecom-template/register.html')

def signin(request):
    return render(request, 'ecom-template/signin.html')

def search_result(request):
    return render(request, 'ecom-template/search-result.html')
