from django.db import models
from django.utils import timezone
from django.apps import apps

from main_apps.apps.workshop.models import SewingWorkshop
from django.utils.translation import gettext_lazy as _


class Warehouse(models.Model):
    """
    Модель для представления склада швейного цеха.
    Логика заказов:

    Создание заказа: Метод для создания нового заказа, который может включать в себя выбор товаров, количество и т.д.
    Отмена заказа: Возможность отмены заказа до его выполнения.
    Отслеживание статуса заказа: Методы для отслеживания статуса заказа, например, "в обработке", "выполнен", "доставлен" и т.д.
    Логика поставок:

    Запрос цены и наличия: Метод для запроса у поставщика цен и наличия товаров.
    Получение поставок: Запись поступления товаров от поставщиков на склад.
    Уведомления о поставках: Уведомление заинтересованных сторон (например, отдела закупок) о поступлении товаров.
    Логика продуктов:

    Добавление новых продуктов: Метод для добавления новых продуктов на склад.
    Управление ассортиментом: Методы для изменения ассортимента товаров на складе.
    Логика отчетности:

    Генерация отчетов: Создание отчетов о текущем состоянии склада, истории поставок, выполненных заказах и т.д.
    Мониторинг и аналитика: Системы мониторинга и аналитики для отслеживания эффективности работы склада.
    Логика безопасности:

    Управление доступом: Ограничение доступа к различным функциям склада в зависимости от ролей пользователя.
    Журналирование действий: Запись действий пользователей для последующего аудита.
    Логика оповещений:

    Уведомления о низких запасах: Автоматические уведомления при достижении определенного уровня запасов.
    Уведомления о событиях: Оповещения о важных событиях, таких как поступление крупной партии товаров или задержка поставок.
    """

    sewing_workshop = models.OneToOneField(
        SewingWorkshop,
        on_delete=models.PROTECT,
        related_name="warehouse",
        verbose_name=_("Цех"),
    )
    # supply_history = models.ManyToManyField(Supply)  # Подставьте свою модель для истории поставок
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Склад - {self.sewing_workshop}"
