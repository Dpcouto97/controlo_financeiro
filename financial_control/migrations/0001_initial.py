# Generated by Django 4.0.5 on 2022-06-10 00:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('descricao', models.CharField(blank=True, max_length=300, null=True)),
                ('valor', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000000), django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoDespesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('descricao', models.CharField(blank=True, max_length=300, null=True)),
                ('valor_normal', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000000), django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField()),
            ],
        ),
    ]
