from django.db import models


class Guest(models.Model):
    STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]

    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Ф.И.О')
    e_mail = models.EmailField(max_length=50, blank=False, null=False, verbose_name='Электронная почта')
    reg_info = models.TextField(max_length=2000, blank=False, null=False, verbose_name='Текст записи')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='active', choices=STATUS_CHOICES, null=False, blank=False)

    class Meta:
        db_table = 'guest'
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'

    def __str__(self):
        return f'{self.status}{self.name}{self.e_mail}{self.reg_info}{self.create_date}{self.update_date}'
