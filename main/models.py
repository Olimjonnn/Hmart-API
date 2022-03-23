from cgitb import text
from itertools import product
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type = models.IntegerField(choices=(
        (1, 'worker'),
        (2, 'client'),
    ), default=2)
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        verbose_name = "User"
        verbose_name_plural = "Users"

class Logo(models.Model):
    image = models.ImageField(upload_to="Logo/")

class Slider(models.Model):
    img = models.ImageField(upload_to="Slider/")
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=217)

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Advertisement(models.Model):
    img = models.ImageField(upload_to="Advertisement/")
    category = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=217)
    price = models.IntegerField()
    sale = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img1 = models.ImageField(upload_to="Product/")
    img2 = models.ImageField(upload_to="Product/", blank=True, null=True)
    img3 = models.ImageField(upload_to="Product/", blank=True, null=True)
    img4 = models.ImageField(upload_to="Product/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_new = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="image/")

    def __str__(self) -> str:
        return self.name

class Brands(models.Model):
    image = models.ImageField(upload_to="Brands/")

class LatestBlog(models.Model):
    image = models.ImageField(upload_to="LatestBlog/")
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=170)
    text = models.CharField(max_length=250)
    date = models.DateField(null=True, default=1)

class Links(models.Model):
    text = models.CharField(max_length=250)
    facebook = models.CharField(max_length=300)
    telegram = models.CharField(max_length=300)
    twitter = models.CharField(max_length=300)
    instagram = models.CharField(max_length=300)

class ContactInfo(models.Model):
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()

class Client(models.Model):
    name = models.CharField(max_length=200) 
    def __str__(self):
        return self.name

class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Wishlist(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)