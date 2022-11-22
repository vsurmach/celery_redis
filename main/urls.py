from django.urls import path
from .views import get_page, get_wind, get_room

urlpatterns = [
    path('', get_page, name='get_page'),
    path('chat/', get_wind),
    path('<str:room_name>/', get_room),
]