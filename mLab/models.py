from django.db import models


# Create your models here.

class Mlab(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    mLab_name = models.CharField(max_length=255)
    mLab_city_location = models.CharField(max_length=255)
    mLab_department = models.CharField(max_length=255)
    clinical_condition = models.CharField(max_length=255)
    session_videos = models.CharField(max_length=255)
    session_drs = models.CharField(max_length=255)

    def __str__(self):
        return self.mLab_name
