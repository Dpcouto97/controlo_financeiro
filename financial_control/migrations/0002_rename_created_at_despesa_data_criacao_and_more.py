# Generated by Django 4.0.5 on 2022-06-10 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial_control', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='despesa',
            old_name='created_at',
            new_name='data_criacao',
        ),
        migrations.RenameField(
            model_name='despesa',
            old_name='created_by',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='tipodespesa',
            old_name='created_at',
            new_name='data_criacao',
        ),
        migrations.RenameField(
            model_name='tipodespesa',
            old_name='created_by',
            new_name='user',
        ),
    ]