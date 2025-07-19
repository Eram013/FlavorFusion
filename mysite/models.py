
from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    quantity=models.IntegerField()
    image= models.CharField(max_length=255000)
    class Meta:
        db_table="user"
    
class user2(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)
    class Meta:
        db_table="user2"


        
