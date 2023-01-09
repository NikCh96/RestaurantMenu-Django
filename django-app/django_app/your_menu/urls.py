from .views import*
from django.urls import path

urlpatterns = [
    path('', menu, name= 'menu'),
    path('menu/<int:post_id>/', show_menu , name = 'show'),
]