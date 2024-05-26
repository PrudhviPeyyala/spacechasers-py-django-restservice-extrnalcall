from django.db import models


# Create your models here.clear
class OemDetail(models.Model):
    manufacturer = models.TextField()
    oemModel = models.TextField()
    yearModel = models.IntegerField(max_length=4)
    origin = models.CharField(max_length=50)

    def __str__(self):
        return self.manufacturer

