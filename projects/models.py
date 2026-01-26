from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    target_budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name