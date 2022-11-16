from django.urls import path
from .views import add_archive, message_list

app_name = 'user_message'

urlpatterns = [
    path('', message_list, name='message_list'),
    path('update/<int:pk>/', add_archive, name='add_archive')
]
