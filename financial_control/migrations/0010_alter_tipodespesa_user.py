# Generated by Django 4.0.5 on 2022-06-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_control', '0009_alter_tipodespesa_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipodespesa',
            name='user',
            field=models.IntegerField(blank=True),
        ),
    ]
