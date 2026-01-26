from django.urls import path, include

from categories.views import categories_list
from expenses.views import expenses_per_category

app_name = 'categories'

urlpatterns = [
    path('', categories_list, name='list'),
    path('<int:category_id>/', expenses_per_category, name='expenses_per_category'),
]