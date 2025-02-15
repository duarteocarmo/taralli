from django.db import models
from django.utils import timezone


class Weight(models.Model):
    weight = models.FloatField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.weight} kg on {self.date}"


class Meal(models.Model):
    description = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    calories = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.description} on {self.date}"
