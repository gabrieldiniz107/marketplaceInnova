# Generated by Django 5.1 on 2024-12-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investimentos', '0003_ativo_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ativo',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
