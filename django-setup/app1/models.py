from django.db import models # type: ignore

# Create your models here.

class SoilmoistureReading(models.Model):
    timeStamp = models.DateTimeField(auto_now_add= True)
    soil_level = models.FloatField(null=True)
