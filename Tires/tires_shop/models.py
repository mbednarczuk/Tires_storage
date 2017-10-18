from django.db import models
from django.contrib.auth.models import User

SEASON = (
    (1, "Summer"),
    (2, "Winter"),
    (3, "All-Season"),
)

LOAD = (
    (1, "Normall"),
    (2, "Cargo"),
)

MONTH = (
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December"),
)


class Tires(models.Model):
    width = models.IntegerField(null=False)
    aspect_ratio = models.IntegerField(null=False)
    diameter = models.IntegerField(null=False)
    tire_brand = models.CharField(max_length=256)
    tire_model = models.CharField(max_length=256)
    production_month = models.IntegerField(choices=MONTH, verbose_name="Month")
    production_year = models.IntegerField(null=False)
    season_type = models.IntegerField(choices=SEASON, verbose_name="Which season ?")
    type_of_load = models.IntegerField(choices=LOAD, verbose_name="Load")
    price = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)

    class Meta:
        verbose_name = "Tire"
        verbose_name_plural = "Tires"

    def __str__(self):
        return ' '.join([self.tire_brand, self.tire_model])
