from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    color = models.CharField(max_length=50)
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.age} years old)"


class Owner(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)


    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        ordering = ['name']