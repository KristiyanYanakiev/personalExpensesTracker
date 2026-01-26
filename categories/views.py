from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from categories.models import Category


# Create your views here.
def categories_list(request: HttpRequest) -> HttpResponse:

    categories = Category.objects.all()
    context = {
        'all_categories': categories
    }
    return render(request, 'categories/list.html', context)
