from django.shortcuts import render
from .models import Item
from django.core.paginator import Paginator
from django.db.models.functions import Lower

def item_list(request):
    #Sorting
    sort_by = request.GET.get('sort', 'name')
    if sort_by not in ['name', '-name', 'price', '-price', 'created_at', '-created_at']:
        sort_by = 'name'

    if 'name' in sort_by:
        if sort_by.startswith('-'):
            items = Item.objects.all().annotate(lower_name=Lower('name')).order_by('-lower_name')
        else:
            items = Item.objects.all().annotate(lower_name=Lower('name')).order_by('lower_name')
    else:
        items = Item.objects.all().order_by(sort_by)

    # Pagination
    paginator = Paginator(items, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj, 'sort_by': sort_by})
