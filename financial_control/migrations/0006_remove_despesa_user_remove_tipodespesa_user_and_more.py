# Generated by Django 4.0.5 on 2022-06-10 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial_control', '0005_remove_despesa_data_criacao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='despesa',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tipodespesa',
            name='user',
        ),
        migrations.AlterField(
            model_name='despesa',
            name='tipo_despesa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='financial_control.tipodespesa'),
        ),
        migrations.AlterField(
            model_name='tipodespesa',
            name='valor_normal',
            field=models.FloatField(null=True),
        ),
    ]