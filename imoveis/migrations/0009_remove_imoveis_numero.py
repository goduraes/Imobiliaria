# Generated by Django 2.2.2 on 2019-06-22 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0008_auto_20190622_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imoveis',
            name='numero',
        ),
    ]
