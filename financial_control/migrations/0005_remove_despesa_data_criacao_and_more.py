# Generated by Django 4.0.5 on 2022-06-10 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial_control', '0004_alter_despesa_data_criacao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='despesa',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='tipodespesa',
            name='data_criacao',
        ),
    ]
