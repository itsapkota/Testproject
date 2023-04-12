from django.db import models

# Create your models here.

class Shop(models.Model):
  shop_name = models.CharField(max_length=255, null=True, blank=True)
  latitude = models.CharField(max_length=255, null=True, blank=True)
  longitude = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self) -> str:
    return self.shop_name