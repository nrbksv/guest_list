# Generated by Django 3.1.7 on 2021-03-06 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_in', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Ф.И.О'),
        ),
    ]
