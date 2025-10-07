from django.contrib import admin
from django.urls import path, include
# from store import views as storeviews
from shop import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),  # Home page
    path('store/', include("shop.store_url")),  # Store listing
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),  # Cart page
    path('place-order/', views.place_order, name='place_order'),  # Place order page
    path('order-complete/', views.order_complete, name='order_complete'),  # Order complete
    path('dashboard/', views.dashboard, name='dashboard'),  # User dashboard
    path('register/', views.register, name='register'),  # User registration
    path('signin/', views.signin, name='signin'),  # User login
    path('search/', views.search_result, name='search_result'),  # Search results
    # path('category/<slug:slug>/', views.category_view, name='category_detail'),
    # path('product/<slug:product_slug>/', storeviews.product_view, name='product_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
