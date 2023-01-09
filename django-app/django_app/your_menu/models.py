from django.db import models
from django.urls import reverse

class Food(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", null=True)
    content = models.CharField(max_length=255, verbose_name="граммы", null=True)
    price = models.CharField(max_length=255, verbose_name="цена",null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Блюда'
        verbose_name_plural = 'Блюда'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show', kwargs={'post_id': self.id})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']