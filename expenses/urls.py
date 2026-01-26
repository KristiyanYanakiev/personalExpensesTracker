from django.urls import path

from expenses.views import all_expenses

app_name = 'expenses'

urlpatterns = [
    path('', all_expenses, name='list' )
]