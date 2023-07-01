# Generated by Django 4.2 on 2023-07-01 18:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventacarta', '0002_carta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCarta', models.PositiveIntegerField(null=True)),
                ('preciototal', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='carta',
            name='imagen',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='contrasenia',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='idventa',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='carta',
            name='anio',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AlterField(
            model_name='carta',
            name='nombre',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='carta',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fNac',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1920), django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombreu',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
