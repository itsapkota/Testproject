from django.shortcuts import render, redirect, get_object_or_404
from math import radians, sin, cos, sqrt, atan2
from django.contrib import messages
from .models import Shop
from .forms import ShopForm, ShowNearbyShop

def shop_list(request):
	queryset = Shop.objects.all()
	return render(request, 'shop_list.html',{'shops': queryset})

def create_shop(request):
	if request.method == "POST":
		shop_form = ShopForm(request.POST)
		if shop_form.is_valid():
			shop_form.save()
			return redirect(".")
		else:
			print("form invalid")
	shop_form = ShopForm()
	return render(request, 'create_shop.html', {'form':shop_form})

def update_shop(request, pk):
	shop = get_object_or_404(Shop, pk=pk)
	if request.method == "POST":
		shop_form = ShopForm(request.POST, instance=shop)
		if shop_form.is_valid():
			shop_form.save()
			messages.success(request, "shop updated successfully.")
			return redirect(".")
		else:
			messages.warning(request, "Please enter a valid data.")
	shop_form = ShopForm(instance=shop)
	return render(request, 'update_shop.html', {'form':shop_form})

def show_nearby_shop(request):
	form = ShowNearbyShop(request.GET)
	current_lat = form.data.get('latitude', None)
	current_lon = form.data.get('longitude', None)
	max_distance = form.data.get('distance', None)

	context = {
				'form': form,
				'shop_name': None,
				'distance': None
			}

	if not current_lat or not current_lon or not max_distance:
		messages.warning(request, "please enter all details")
	else:
		current_lat = float(current_lat)
		current_lon = float(current_lon)
		max_distance = float(max_distance)

		# maximum distance (in meters)
		max_distance = max_distance*1000

		shops = Shop.objects.all()
		nearby_shops = []
		# loop through all the shops
		for shop in shops:
			shop_lat = float(shop.latitude)
			shop_lon = float(shop.longitude)
			
			# calculate the distance using the Haversine formula
			d_lat = radians(shop_lat - current_lat)
			d_lon = radians(shop_lon - current_lon)
			a = sin(d_lat / 2) ** 2 + cos(radians(current_lat)) * cos(radians(shop_lat)) * sin(d_lon / 2) ** 2
			c = 2 * atan2(sqrt(a), sqrt(1 - a))
			distance = 6371 * c  # multiply by 6371 to get distance in km
			
			# check if the shop is within the specified distance
			if distance <= max_distance/1000:
				nearby_shops.extend([shop.shop_name])
			
		if nearby_shops:
			messages.success(request, f'found {len(nearby_shops)} shops.')
			context['shop_name'] = nearby_shops
		if max_distance:
			context['distance'] = max_distance/1000
	return render(request, 'show_nearby_shop.html', context)


