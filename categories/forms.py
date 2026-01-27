from enum import unique

from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100
    )

class CreateCategoryForm(forms.Form):
    name = forms.CharField(
        label='Enter the name of the category',
        max_length=100,

    )

    monthly_budget = forms.DecimalField(
        label='',
        max_digits=10,
        decimal_places=2,
        required=False
    )

    description = forms.CharField(
        label='',
        required=False
    )




