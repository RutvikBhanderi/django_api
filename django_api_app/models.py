from django.db import models

class student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100,default="")
    age = models.IntegerField(default=0)
    email = models.CharField(max_length=100,default="")
    phone = models.BigIntegerField(default=0)
    city = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to="")

