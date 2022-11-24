from django.db import models

class Listing(models.Model):
    neighbourhood_group = models.CharField(max_length=20)
    neighbourhood = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.neighbourhood_group
