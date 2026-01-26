from django.core.validators import MinValueValidator
from django.db import models

from expenses.validators import validate_dat_not_future


# Create your models here.
class Expense(models.Model):
    title = models.CharField(
        max_length=100,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01, message='Amount must be positive')]
    )
    date = models.DateTimeField(
        auto_now_add=True,
        validators=[validate_dat_not_future]
    )
    category = models.ForeignKey(
        to='categories.Category',
        on_delete=models.PROTECT,
        related_name='expenses'
    )

    projects = models.ManyToManyField(
        to='projects.Project',
        blank=True,
        related_name='expenses'
    )
    notes = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.title} - {self.amount}"