
from unicodedata import category

from .models import Category

def menu_links(request):
    links = Category.objects.all()  #TODO: query this
    return dict(links=links)