# Generated by Django 2.2.2 on 2019-06-22 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alugados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_cliente', models.IntegerField(blank=True, null=True, verbose_name='Número do imóvel')),
                ('fk_imovel', models.IntegerField(blank=True, null=True, verbose_name='Número do imóvel')),
            ],
        ),
    ]
