from django.urls import path
from .views import reservation_list, reservation_close, home

app_name = 'manager'

urlpatterns = [
    path('', reservation_list, name='reservation_list'),
    path('update/<int:pk>/', reservation_close, name='reservation_close'),
    path('index.html', home, name='home'),
]
