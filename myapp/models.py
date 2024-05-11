from django.db import models

# Create your models here.


class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    photo = models.CharField(max_length=500,default="A")

class Suggestion(models.Model):
    compaint=models.CharField(max_length=100)
    response=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)

class Category(models.Model):
    catname=models.CharField(max_length=100)

class Dress(models.Model):
    dname=models.CharField(max_length=100)
    photo=models.CharField(max_length=500)
    description=models.CharField(max_length=100)
    CATEGORY=models.ForeignKey(Category,on_delete=models.CASCADE)
    skintone=models.CharField(max_length=100)
    bodytype=models.CharField(max_length=500,default="")
    gender=models.CharField(max_length=100,default="")
    occasions = models.CharField(max_length=100, default="")

class SkinProducts(models.Model):
    pname=models.CharField(max_length=100)
    photo=models.CharField(max_length=500)
    description=models.CharField(max_length=100)
    CATEGORY=models.ForeignKey(Category,on_delete=models.CASCADE)
    skintone=models.CharField(max_length=100)
    skinType=models.CharField(max_length=500,default="")
    gender=models.CharField(max_length=100,default="")
    occasions = models.CharField(max_length=100, default="")

class Mydress(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    dressphoto=models.CharField(max_length=300)
    dresstype=models.CharField(max_length=100)



