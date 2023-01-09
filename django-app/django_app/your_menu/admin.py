from django.contrib import admin
from .models import*
from django.utils.safestring import mark_safe
# user: honor, password: honor


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    fields = ('name',)

admin.site.register(Category, CategoryAdmin)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','price','cat')
    list_display_links = ('title', 'content','price','cat')
    search_fields = ('title', 'content','price','cat')
    fields = ('title', 'content','price','cat')

admin.site.register(Food, FoodAdmin)

    # def get_html_photo(self, object):
    #     if object.photo:
    #         return mark_safe(f"<img src='{object.photo.url}' width=100>")

    # get_html_photo.short_description = 'Фото'



