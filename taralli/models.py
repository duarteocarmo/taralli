from django.db import models


class Weight(models.Model):
    weight = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.weight} kg on {self.date}"


class Meal(models.Model):
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    calories = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.description} on {self.date}"
