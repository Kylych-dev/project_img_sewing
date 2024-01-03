from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from apps.account.validation import INNValidator
from apps.workshop.models import SewingWorkshop


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        SEAMSTRESS = "seamstress", _("Швея")
        TECHNOLOGIST = "technologist", _("Технолог")
        IRON_WORKER = "iron_worker", _("Утюжник")
        DIRECTOR = "director", _("Директор")
        BUTTON_ATTACHER = "button_attacher", _("Пуговщик")
        PACKER = "packer", _("Упаковщик")
        WAREHOUSEMAN = "Warehouseman", _("Складовщик")
        CUTTER = "Cutter", _("Кройщик")

    inn_validator = INNValidator()

    username = models.CharField(
        verbose_name=_("ИНН"),
        max_length=14,
        unique=True,
        help_text=_("Обязательное поле. Должно содержать 14 цифр"),
        validators=[inn_validator],
        error_messages={
            "unique": _("Пользователь с таким ИНН уже существует."),
        },
    )
    passport_pic = models.ImageField(
        verbose_name=_("Фото пасспорта для верификации"),
        upload_to='passport/pic',
        null=True, blank=True,
    )
    profile = models.ImageField(
        upload_to='profile/',
        null=True,
        blank=True,
        verbose_name=_("Profile")
    )
    role = models.CharField(
        choices=Role.choices,
        default=Role.SEAMSTRESS,
        max_length=30,
        verbose_name=_("Роль сотрудника"),
    )
    phone_number = models.CharField(verbose_name=_("Номер телефона"), max_length=20)
    sewing_workshop = models.ForeignKey(
        SewingWorkshop,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Швейный цех"),
        related_name="sewing_workshop",
    )
    work_status = models.BooleanField(
        verbose_name=_("Статус наличия работы"),
        default=True,
        help_text="Если статус True то у человека есть место работы",
    )  # todo Поменять на enum стаус  пример, В поисках работы, есть работа, и т.д

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"

