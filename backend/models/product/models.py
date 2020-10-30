from django.db import models

class Product(models.Model):
    id = models.AutoField( primary_key = True)
    photo = models.ImageField(null=True)
    name = models.CharField( max_length = 50)
    provider = models.CharField( max_length = 50)
    category = models.CharField( max_length = 50)
    price = models.FloatField()

    def __str__(self): 
        return self.name