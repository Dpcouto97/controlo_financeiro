# Generated by Django 4.0.5 on 2022-06-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_control', '0019_despesa_data_criacao_despesa_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='valor',
            field=models.DecimalField(decimal_places=3, max_digits=7, null=True),
        ),
    ]
