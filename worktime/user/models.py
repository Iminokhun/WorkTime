from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Организация')
    stat_time = models.TimeField(blank=False)
    end_time = models.TimeField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    login = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class WorkHours(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    start_time = models.TimeField(auto_now_add=True, verbose_name='Время работы')
    end_time = models.TimeField(auto_now_add=True, verbose_name='Время оканчания')
    total_hours = models.FloatField(verbose_name='Обшее кол часов')

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'


