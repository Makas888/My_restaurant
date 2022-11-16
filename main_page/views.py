from django.shortcuts import render, redirect
from .models import Category, Dish, All_Inform, Event, Gallery, InformationRestaurant,\
                    Personal, Testimonials, HeroSection
import random
from .forms import UserReservationForm, UserMessageForm


def main_view(request):
    form_reserve = UserReservationForm(request.POST or None)

    if form_reserve.is_valid():
        form_reserve.save()
        return redirect('/')

    form_user_message = UserMessageForm(request.POST or None)

    if form_user_message.is_valid():
        form_user_message.save()
        return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    specials = Dish.objects.filter(is_visible=True, is_special=True)
    whu_us = All_Inform.objects.filter(is_visible=True)
    abouts = All_Inform.objects.filter(position=False, is_visible=False)
    events = Event.objects.all()
    galleries = Gallery.objects.all()
    galleries = random.sample(list(galleries), 8)
    information = InformationRestaurant.objects.filter(is_visible=True)
    personals = Personal.objects.filter(is_visible=True)
    testimonials = Testimonials.objects.filter(is_visible=True)
    hero_sections = HeroSection.objects.filter(is_visible=True)

    return render(request, 'base.html', context={
        'form_user_message': form_user_message,
        'form_reserve': form_reserve,
        'categories': categories,
        'dishes': dishes,
        'specials': specials,
        'whu_us': whu_us,
        'abouts': abouts,
        'events': events,
        'galleries': galleries,
        'information': information,
        'personals': personals,
        'testimonials': testimonials,
        'hero_sections': hero_sections,
    })
