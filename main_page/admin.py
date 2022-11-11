from django.contrib import admin
from .models import Category, Dish, Event, All_Inform, Gallery, InformationRestaurant,\
    Personal, Testimonials, HeroSection
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', )


admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Event)
admin.site.register(All_Inform, PostAdmin)
admin.site.register(Gallery)
admin.site.register(InformationRestaurant)
admin.site.register(Personal)
admin.site.register(Testimonials)
admin.site.register(HeroSection)
