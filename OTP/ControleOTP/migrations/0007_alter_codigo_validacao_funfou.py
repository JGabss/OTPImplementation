# Generated by Django 3.2 on 2021-12-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControleOTP', '0006_codigo_validacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigo_validacao',
            name='funfou',
            field=models.CharField(max_length=10),
        ),
    ]