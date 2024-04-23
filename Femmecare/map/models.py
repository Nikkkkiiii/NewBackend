from django.db import models
class MapMarker(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()

    def __str__(self):
        return self.address


