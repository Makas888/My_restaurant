from django.shortcuts import render
from .models import Category, Dish, All_Inform, Event, Gallery
import random


def main_view(request):

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    specials = Dish.objects.filter(is_visible=True, is_special=True)
    whu_us = All_Inform.objects.filter(is_visible=True)
    abouts = All_Inform.objects.filter(position=False, is_visible=False)
    events = Event.objects.all()
    galleries = Gallery.objects.all()
    galleries = random.sample(list(galleries), 8)

    return render(request, 'base.html', context={
        'categories': categories,
        'dishes': dishes,
        'specials': specials,
        'whu_us': whu_us,
        'abouts': abouts,
        'events': events,
        'galleries': galleries,
    })
