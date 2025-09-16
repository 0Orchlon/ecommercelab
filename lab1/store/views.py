# store/views.py
from django.shortcuts import render, get_object_or_404
# from .models import Category, Product


# def index(request):
#     categories = Category.objects.all()
#     return render(request, "store/index.html", {"categories": categories})

def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, is_available=True)
    return render(request, "store/category.html", {"category": category, "products": products})

# def product_view(request, product_slug):
#     product = get_object_or_404(Product, slug=product_slug, is_available=True)
#     return render(request, "store/product.html", {"product": product})
def product_view(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, is_available=True)
    category = product.category  # get its category
    return render(
        request,
        "store/product.html",
        {"product": product, "category": category}
    )
