from django.db import models

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cards(models.Model):
    category = models.ForeignKey(Categories,null=True,blank=True,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='uploads/')
    card_name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.card_name

class Carousel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return self.name

class CardsCategory(models.Model):
    category = models.ForeignKey(Categories, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    urls = models.CharField(max_length=100)

    def __str__(self):
        return self.name