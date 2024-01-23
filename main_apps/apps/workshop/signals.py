from django.db.models.signals import post_save
from django.dispatch import receiver

from main_apps.apps.warehouse.models import Warehouse
from main_apps.apps.workshop.models import SewingWorkshop
from main_apps.apps.account.models import CustomUser


@receiver(post_save, sender=SewingWorkshop)
def sewing_workshop_warehouse_create(sender, instance, created, **kwargs):
    if created:
        Warehouse.objects.create(sewing_workshop=instance)


@receiver(post_save, sender=CustomUser)
def sewing_workshop_customuser_create(sender, instance, created, **kwargs):
    if created:
        # Создание нового цеха
        workshop = SewingWorkshop.objects.create(name='Название цеха')

        # Связывание пользователя с созданным цехом и сохранение номера телефона
        instance.sewing_workshop = workshop
        instance.save(update_fields=['sewing_workshop'])  # Обновление поля sewing_workshop

        # Сохранение номера телефона в цехе
        workshop.phone_number = instance.phone_number
        workshop.save(update_fields=['phone_number']) # Обновление поля phone_number