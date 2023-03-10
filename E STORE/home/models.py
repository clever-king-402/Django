from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    icon = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    icon = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Ad(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    rank = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
	name = models.CharField(max_length = 400)
	image = models.ImageField(upload_to = 'media')

	def __str__(self):
		return self.name


STOCK = (('in','In Stock'),('out','Out of Stock'))
LABELS = (('hot','hot'),('sale','sale'),('new','new'),('','default'))

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,blank=True)

    stock = models.CharField(choices=STOCK,max_length=100)
    labels = models.CharField(choices=LABELS,max_length=100)



