from django.db import models

from django.db import models

class MapMarker(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
