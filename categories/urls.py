from django.urls import path, include

from categories.views import categories_list, create_category, edit_category, delete_category
from expenses.views import expenses_per_category

app_name = 'categories'

urlpatterns = [
    path('', categories_list, name='list'),
    path('create_category/', create_category, name= 'create_category'),
    path('<int:category_id>/', expenses_per_category, name='expenses_per_category'),
    path('<int:category_id>/edit_category', edit_category, name='edit_category'),
    path('<int:category_id>/delete_category', delete_category, name='delete_category')
]