# Generated by Django 2.2.2 on 2019-06-28 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alugados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alugados',
            name='fk_cliente',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='alugados',
            name='fk_imovel',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Imóvel'),
        ),
    ]
