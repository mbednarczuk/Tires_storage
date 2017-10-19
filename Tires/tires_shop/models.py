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

PRICE_GROUP = (
    (1, "budget"),
    (2, "middle"),
    (3, "premium"),
    (4, "other"),
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
    image = models.ImageField(upload_to='tire_image', blank=True)

    class Meta:
        verbose_name = "Tire"
        verbose_name_plural = "Tires"

    def __str__(self):
        return ' '.join([self.tire_brand])


class BrandsDescribe(models.Model):
    brand_name = models.ForeignKey(Tires)
    origin_country = models.CharField(max_length=256)
    company = models.CharField(max_length=256)
    price_group = models.IntegerField(choices=PRICE_GROUP, verbose_name="Price group")
    describe = models.TextField()

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Order(models.Model):
    order_tire = models.ForeignKey(Tires, verbose_name="order_tire")
    quantity = models.DecimalField(max_digits=5, decimal_places=0)
    user = models.ForeignKey(User)

    def __str__(self):
        return ' '.join([self.user])
