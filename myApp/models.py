from django.db import models


# Create your models here.

class Mlab(models.Model):
    unique_id = models.CharField(max_length=255, unique=True)
    mLab_name = models.CharField(max_length=255)
    mLab_city_location = models.CharField(max_length=255)
    mLab_department = models.CharField(max_length=255)
    clinical_condition = models.CharField(max_length=255)

    def __str__(self):
        return self.mLab_name
