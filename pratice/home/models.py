from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self) -> str:
        return self.name
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    percent = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class Work(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

