from django.db import models


class TelephoneModel(models.Model):
    price = models.IntegerField()
    model = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey("Brand",on_delete=models.CASCADE,related_name="phones",blank=True,null=True)
    case = models.ManyToManyField("Case",related_name="cases",blank=True,null=True)
    def __str__(self):
        return self.model

class Brand(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Case(models.Model):
    color = models.CharField(max_length=100)
    size = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.color}-{self.price}"




