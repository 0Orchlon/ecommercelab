from django.urls import path
# from store import views as storeviews
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.store, name='store'),  # Store listing
    path('<slug:slug>', views.store, name='store'),  # Store listing
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
