from django.db import models
from django.contrib.auth.models import AbstractUser

class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Организация')
    stat_time = models.TimeField(blank=False)
    end_time = models.TimeField(blank=False)
    qr_code = models.ImageField(verbose_name='QR код', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

class User(AbstractUser):
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE)
    login = models.EmailField(unique=True,)


    # def __str__(self):
    #     return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class WorkHours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.TimeField(auto_now_add=True, verbose_name='Время работы')
    end_time = models.TimeField(auto_now_add=True, verbose_name='Время оканчания')
    total_hours = models.FloatField(verbose_name='Обшее кол часов')

    def __str__(self):
        return self.created_at


