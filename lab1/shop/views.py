from django.shortcuts import render
# adjust if your models are in a different app
from store.models import Category, Product
from django.shortcuts import render, get_object_or_404



def index(request):
    categories = Category.objects.raw("SELECT * FROM store_category")
    products = Product.objects.raw("""
        SELECT * FROM store_product
        ORDER BY created_date DESC
        LIMIT 4
    """)
        # WHERE is_available = TRUE
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'ecom-template/index.html', context)
    
def store(request, slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    sort = request.GET.get('sort')

    # Filter by category slug from the URL (not GET params)
    selected_category = slug
    if slug:
        products = products.filter(category__slug=slug)

    # Sort logic
    if sort == 'recent':
        products = products.order_by('-created_date')
    elif sort == 'oldest':
        products = products.order_by('created_date')

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'ecom-template/store.html', context)


def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    return render(request, 'ecom-template/product-detail.html', {'product': product})

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
