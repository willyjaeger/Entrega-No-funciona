# Generated by Django 4.2.3 on 2023-08-31 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nombreusuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
