from django.db import models


class TelephoneModel(models.Model):
    price = models.IntegerField()
    model = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    type = models.ForeignKey("Brand",on_delete=models.CASCADE,related_name="phone",blank=True,null=True)

class Brand(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)




