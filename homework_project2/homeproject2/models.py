from django.db import models

# Create your models here.
class TelephoneModel(models.Model):
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    model = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

