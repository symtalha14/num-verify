from django.db import models

# Create your models here.

class Demo(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField(default=0)
    email = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Country(models.Model):
    country_num_code =  models.CharField(max_length=50)
    country_alpha_1_code =  models.CharField(max_length=50)
    country_alpha_2_code =  models.CharField(max_length=50) 
    country_name = models.TextField(max_length=None)
    phone_prefix = models.IntegerField(default=0)
    phone_length = models.CharField(max_length=100)
    def __str__(self):
        return self.country_alpha_2_code