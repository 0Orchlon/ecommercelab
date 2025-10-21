from store.models import *
from carts.models import *

def menulinks(request):
    links = Category.objects.all()
    return dict(links = links)

def cart_total_items(request):
    total_quantity = 0
    try:
        cart_id = request.session.session_key
        if not cart_id:
            cart_id = request.session.create()
        cart = Cart.objects.get(cart_id=cart_id)
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        total_quantity = sum(item.quantity for item in cart_items)
    except Cart.DoesNotExist:
        total_quantity = 0
    return {'cart_total_quantity': total_quantity}
