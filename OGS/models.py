from django.db import models


class GoodsServices(models.Model):
    def __str__(self):
        return self.name[0:50]

    name = models.TextField(max_length=1000)


class Organization(models.Model):
    def __str__(self):
        return self.name

    service = models.ManyToManyField(GoodsServices)
    name = models.CharField(max_length=100)