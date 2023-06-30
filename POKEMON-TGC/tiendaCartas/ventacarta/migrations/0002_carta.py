# Generated by Django 4.2 on 2023-06-30 17:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventacarta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('anio', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)])),
                ('precio', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
