from django.conf import settings
from django.db import models


class Taxis(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    carNumber = models.CharField(max_length=6)
    carBrand = models.CharField(max_length=50)
    tariff = models.CharField(max_length=50)
    salary = models.FloatField()


class Order(models.Model):
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    distance = models.FloatField()
    cost = models.FloatField()
    tariff = models.CharField(max_length=50)
    passenger = models.IntegerField()
    taxis = models.IntegerField()


class Tariff(models.Model):
    name = models.CharField(max_length=50)
    costKm = models.FloatField()


class DateTime(models.Model):
    date = models.DateField()
    time = models.TimeField()


# Create your models here.
