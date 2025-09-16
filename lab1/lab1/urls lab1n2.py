from django.contrib import admin
from django.urls import path
from shop.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),  # Home page
    path('store/', views.store, name='store'),  # Store listing
    path('product/', views.product_detail, name='product_detail'),  # Product detail
    path('cart/', views.cart, name='cart'),  # Cart page
    path('place-order/', views.place_order, name='place_order'),  # Place order page
    path('order-complete/', views.order_complete, name='order_complete'),  # Order complete
    path('dashboard/', views.dashboard, name='dashboard'),  # User dashboard
    path('register/', views.register, name='register'),  # User registration
    path('signin/', views.signin, name='signin'),  # User login
    path('search/', views.search_result, name='search_result'),  # Search results
]
