from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_agent = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    date_posted = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="images")
    image_url = models.URLField()

class Favorite(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="favorites")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    date_added = models.DateTimeField(auto_now_add=True)

class Inquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="inquiries")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inquiries")
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
