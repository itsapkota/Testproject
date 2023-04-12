from django import  forms
from .models import Shop

class ShopForm(forms.ModelForm):
  class Meta:
    model = Shop
    fields = "__all__"

class ShowNearbyShop(forms.Form):
  latitude = forms.CharField(max_length=255)
  longitude = forms.CharField(max_length=255)
  distance = forms.CharField(max_length=255)