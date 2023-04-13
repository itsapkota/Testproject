from django import  forms
from .models import Shop

class ShopForm(forms.ModelForm):
  class Meta:
    model = Shop
    fields = "__all__"

class ShowNearbyShop(forms.Form):
  latitude = forms.DecimalField(max_digits=9, decimal_places=6)
  longitude = forms.DecimalField(max_digits=9, decimal_places=6)
  distance = forms.DecimalField(max_digits=9, decimal_places=6)