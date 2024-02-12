from .models import Item

def book_item():
    query = Item.objects.get()
