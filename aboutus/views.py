from django.shortcuts import render, get_object_or_404
from .models import AboutUs

def about_us(request):
	about_us = AboutUs.objects.filter(is_active=True)[0]

	title = about_us.title
	short_description = about_us.short_description
	description = about_us.description
	context = {
			'title': title,
			'short_description': short_description,
			'description': description,
		}

	return render(request, 'about_us/about_us.html', context)