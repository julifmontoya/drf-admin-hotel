from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    num_rooms = models.IntegerField()
    stars = models.IntegerField()
    address = models.CharField(max_length=100)
    latitude = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=11, decimal_places=8, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


