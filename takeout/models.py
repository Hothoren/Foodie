from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

'''class User(models.Model):
    user_id = models.CharField(max_length = 12,null = False,primary_key = True)
    user_password = models.CharField(max_length = 16,null = False)
    user_school = models.CharField(max_length = 20)'''
class DeliveryMan(models.Model):
    deliveryman_id = models.CharField(max_length = 12,null = False,primary_key = True)
    deliveryman_name = models.CharField(max_length = 20)

class Shop(models.Model):
    shop_id = models.CharField(max_length = 12,null = False,primary_key = True)
    shop_name = models.CharField(max_length = 20)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,null = True)
    
class Ident(models.Model):
    ident_id = models.CharField(max_length = 20,null = False,primary_key = True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,null = True)
    deliveryman_id = models.ForeignKey(DeliveryMan,null = True)
    
class Food(models.Model):
    food_id = models.CharField(max_length = 15,null = False,primary_key = True)
    food_name = models.CharField(max_length = 20,null = False)
    shop_id = models.ForeignKey(Shop,null = True)
    
class Ident_Food(models.Model):
    ident_id = models.ForeignKey(Ident)
    food_id = models.ForeignKey(Food)
    food_num = models.IntegerField(null = True)
    class Meta:
        unique_together = ('ident_id','food_id')
    primary = ('ident_id','food_id')

class Dealer(models.Model):
    dealer_id = models.CharField(max_length = 12,null = False,primary_key = True)
    dealer_name = models.CharField(max_length = 20)

class Cart(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    food_id = models.ForeignKey(Food)
    food_num = models.IntegerField(null = True)




