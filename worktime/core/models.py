from django.db import models, migrations
from django.contrib.auth.models import AbstractUser, Permission, User
from django.conf import settings

class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Организация')
    stat_time = models.TimeField(verbose_name='Время начинание работы', blank=False)
    end_time = models.TimeField(verbose_name='Время оканчания работы', blank=False)
    qr_code = models.ImageField(upload_to='qr_code', verbose_name='QR код', blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

class EmployeeUser(User):
    login = models.EmailField(unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class WorkHours(models.Model):
    employee = models.ForeignKey(EmployeeUser, on_delete=models.CASCADE)
    start_time = models.TimeField(auto_now_add=True, verbose_name='Время работы')
    end_time = models.TimeField(auto_now_add=True, verbose_name='Время оканчания')
    total_hours = models.FloatField(verbose_name='Обшее кол часов')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.employee.first_name} {self.employee.last_name}'

    class Meta:
        ordering = ['date', 'start_time']