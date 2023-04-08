from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    url = models.SlugField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.url})


class Car(models.Model):
    model = models.CharField(max_length=150)
    description = models.TextField("description", blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    country = models.CharField(max_length=200)
    image = models.ImageField(upload_to='carImages', null=True)
    price = models.PositiveIntegerField(blank=True)
    volume = models.PositiveSmallIntegerField(blank=True)
    url = models.SlugField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('show', kwargs={'slug': self.category.url, 'url': self.url})
