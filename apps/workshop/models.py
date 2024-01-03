from django.db import models
from django.utils.translation import gettext_lazy as _


class SewingWorkshop(models.Model):
    """
    Модель для представления швейного цеха.

    Описание:
    Эта модель представляет швейный цех и содержит информацию о нем, такую как название.

    """
    name = models.CharField(
        verbose_name=_('Название цеха'),
        unique=True,
        max_length=100)
    slug = models.SlugField(
        verbose_name=_('Название url'),
        unique=True
    )
    phone_number = models.CharField(
        verbose_name=_('Номер телефона'),
        max_length=15)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Швейный цех'
        verbose_name_plural = 'Швейные цеха'
        db_table = 'sewing_workshop'
