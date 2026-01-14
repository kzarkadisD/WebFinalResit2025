from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator
from  users.models import *

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class SubCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    parent_category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Subcategories"

class Product(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128, blank=True)
    price = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(9999)])
    ratingavg = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    image = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"

class Rating(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  # ID of the object being rated
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return f"Rating {self.product_id} - {self.user_id} - {self.rating} "