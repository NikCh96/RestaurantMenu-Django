from django import template
from your_menu.models import*

register = template.Library()


@register.inclusion_tag('show_menu_tag.html')
def show_menu(cat_selected=0):
    menu = Category.objects.select_related
    return {"menu": menu, 'cat_selected': cat_selected}
