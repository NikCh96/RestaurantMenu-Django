from django.shortcuts import render
from .models import*


def menu(request):
    return render(request, 'menu.html')

def show_menu(request, post_id):
    post = Food.objects.select_related
    context = {
        "post": post,
        "post_id": post_id
    }

    return render(request, 'show_menu.html', context = context)
