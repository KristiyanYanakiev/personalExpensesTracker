from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from categories.forms import SearchForm, CreateCategoryForm, EditCategoryForm, DeleteCategoryForm
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
            # Category.objects.create(
            #     name=form.cleaned_data['name'],
            #     monthly_budget=form.cleaned_data["monthly_budget"],
            #     description=form.cleaned_data["description"]
            # )

            form.save()
            return redirect('categories:list')

    context = {
        'form': form
    }

    return render(request, 'categories/create_category.html', context)


def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id )
    form = EditCategoryForm(
        data=request.POST or None,
        instance=category

    )

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('categories:list')

    context = {
        'form': form,
        'category': category
    }

    return render(request, 'categories/edit_category.html', context)

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    form = DeleteCategoryForm(
        instance=category
    )

    if request.method == 'POST':
        category.delete()
        return redirect('categories:list')

    context = {
        'form': form,
        'category': category
    }

    return render(request, 'categories/delete_category.html', context)
