from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    url = models.SlugField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Car(models.Model):
    model = models.CharField(max_length=150)
    description = models.TextField("description", blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    country = models.CharField(max_length=200)
    price = models.PositiveIntegerField(blank=True)
    volume = models.PositiveSmallIntegerField(blank=True)
    url = models.SlugField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
