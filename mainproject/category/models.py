from django.db import models

class Breakfast(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return self.name
