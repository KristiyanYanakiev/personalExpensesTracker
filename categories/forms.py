from enum import unique

from django import forms
from django.db import models

from categories.models import Category


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100
    )

# class CreateCategoryForm(forms.Form):
#     name = forms.CharField(
#         label='Enter the name of the category',
#         max_length=10,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Enter a name'
#             }
#         )
#
#     )
#
#     monthly_budget = forms.DecimalField(
#         label='',
#         max_digits=10,
#         decimal_places=2,
#         required=False,
#         widget=forms.PasswordInput()
#
#     )
#
#     description = forms.CharField(
#         label='',
#         required=False
#     )



class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CreateCategoryForm(CategoryBaseForm):
    ...

class EditCategoryForm(CategoryBaseForm):
    pass

class DeleteCategoryForm(CategoryBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True




