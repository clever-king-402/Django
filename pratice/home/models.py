from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=100)

    def __str__(self) -> str:
        return self.name