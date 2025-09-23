from store.models import *

def menulinks(request):
    links = Category.objects.all()
    return dict(links = links)