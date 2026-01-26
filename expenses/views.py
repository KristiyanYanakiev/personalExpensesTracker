from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from categories.models import Category
from expenses.models import Expense


# Create your views here.
def all_expenses(request: HttpRequest) -> HttpResponse:
    all_expenses = Expense.objects.all()
    context = {
        'all_expenses': all_expenses
    }

    return render(request, 'expenses/list.html', context)

def expenses_per_category(request: HttpRequest, category_id) -> HttpResponse:
    category = get_object_or_404(Category, id=category_id)
    all_expenses_per_category = Expense.objects.filter(category=category)
    context = {
        'all_expenses_per_category': all_expenses_per_category,
        'category': category
    }

    return render(request, 'expenses/expenses_per_category.html', context)