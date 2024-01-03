from django.db import models
from django.utils.translation import gettext_lazy as _

class SizeChoices(models.TextChoices):
    S = 's', _('S')
    M = 'm', _('M')
    L = 'l', _('L')
    XL = 'xl', _('XL')
    XXL = 'xxl', _('XXL')

class Shirt(models.Model):
    """
    Модель для представления товара с характеристиками.

    Пример: Футболка, красная, размера S, M, X, XL
    """
    name = models.CharField(
        verbose_name=_("Название продукта"),
        help_text='Пример: Футболка, Брюки и т.д',
        max_length=255
    )
    color = models.CharField(
        max_length=50,
        verbose_name=_("Цвет"),
        null=True, blank=True
    )
    size = models.CharField(
        max_length=20,
        choices=SizeChoices.choices,
        verbose_name=_('Размер'),
        null=True, blank=True
    )

    def __str__(self):
        return f'{self.name} {self.color} {self.size}'

    class Meta:
        verbose_name = 'Рубашка'
        verbose_name_plural = 'Рубашки'