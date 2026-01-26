from django.db.models import Sum
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from expenses.models import Expense


# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    total_amount = Expense.objects.aggregate(total=(Sum('amount')))['total']
    context = {
        'total_amount': total_amount
    }
    return render(request, 'common/index.html', context)
