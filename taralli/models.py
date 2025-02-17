from django.db import models
from django.utils import timezone


class Weight(models.Model):
    KILOGRAM = 'kg'
    POUND = 'lb'
    UNIT_CHOICES = [
        (KILOGRAM, 'Kilograms'),
        (POUND, 'Pounds'),
    ]

    weight = models.FloatField()
    unit = models.CharField(
        max_length=2,
        choices=UNIT_CHOICES,
        default=KILOGRAM,
    )
    date = models.DateTimeField(default=timezone.now)

    def to_kg(self):
        if self.unit == self.KILOGRAM:
            return self.weight
        return self.weight * 0.45359237

    def to_lb(self):
        if self.unit == self.POUND:
            return self.weight
        return self.weight * 2.20462262

    def __str__(self):
        return f"{self.weight} {self.unit} on {self.date}"


class Meal(models.Model):
    description = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    calories = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.description} on {self.date}"
