# Generated by Django 4.2.3 on 2023-09-03 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0008_entradasblog_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradasblog',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
