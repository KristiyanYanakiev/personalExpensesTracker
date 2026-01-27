from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from categories.forms import SearchForm, CreateCategoryForm
from categories.models import Category


def categories_list(request: HttpRequest) -> HttpResponse:
    form = SearchForm(request.GET or None)
    categories = Category.objects.all()

    if request.method == 'GET':
        if form.is_valid():
            query = form.cleaned_data['query']
            categories = Category.objects.filter(name__icontains=query)

    context = {
        'categories': categories,
        'form': form
    }

    return render(request, 'categories/list.html', context)
def create_category(request):
    form = CreateCategoryForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            Category.objects.create(
                name=form.cleaned_data['name'],
                monthly_budget=form.cleaned_data["monthly_budget"],
                description=form.cleaned_data["description"]
            )
            return redirect('categories:list')

    context = {
        'form': form
    }

    return render(request, 'categories/create_category.html', context)






