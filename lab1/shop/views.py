from django.shortcuts import render
# adjust if your models are in a different app
from store.models import Category, Product
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db import connection



def index(request):
    # --- Get all categories ---
    categories = Category.objects.raw("SELECT * FROM store_category")

    # --- Handle pagination ---
    page = int(request.GET.get("page", 1))
    per_page = 2  # Number of products per page

    # Count total products
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM store_product WHERE is_available = TRUE")
        total_products = cursor.fetchone()[0]

    # Calculate offset
    offset = (page - 1) * per_page

    # --- Get paginated products using raw SQL ---
    products = list(Product.objects.raw(f"""
        SELECT * FROM store_product
        WHERE is_available = TRUE
        ORDER BY created_date DESC
        LIMIT {per_page} OFFSET {offset}
    """))

    # --- Create paginator manually for template compatibility ---
    paginator = Paginator(range(total_products), per_page)
    page_obj = paginator.get_page(page)

    context = {
        'categories': categories,
        'products': products,
        'page_obj': page_obj,  # for pagination buttons
        'total_products': total_products,
    }
    return render(request, 'ecom-template/index.html', context)

def store(request, slug=None):
    categories = Category.objects.all()
    sort = request.GET.get('sort')
    selected_category = slug

    # Base query
    products = Product.objects.filter()

    # Filter by category slug
    if slug:
        products = products.filter(category__slug=slug)

    # Sort logic
    if sort == 'recent':
        products = products.order_by('-created_date')
    elif sort == 'oldest':
        products = products.order_by('created_date')
    else:
        # Default ordering (to fix pagination warning)
        products = products.order_by('id')

    # Pagination AFTER filtering and sorting
    paginator = Paginator(products, 2)  # 6 products per page
    page_number = request.GET.get('page')
    paged_products = paginator.get_page(page_number)

    product_count = products.count()

    context = {
        'products': paged_products,  # Use paginated products
        'categories': categories,
        'selected_category': selected_category,
        'product_count': product_count,
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
