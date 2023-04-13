from django.db import models

# Create your models here.

class Shop(models.Model):
  shop_name = models.CharField(max_length=255)
  latitude = models.DecimalField(max_digits=9, decimal_places=6)
  longitude = models.DecimalField(max_digits=9, decimal_places=6)

  def __str__(self) -> str:
    return self.shop_name