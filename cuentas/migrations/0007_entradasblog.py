# Generated by Django 4.2.3 on 2023-09-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0006_mensajes'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntradasBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=40)),
                ('subtitulo', models.CharField(default='', max_length=40)),
                ('contenido', models.CharField(default='', max_length=100)),
                ('usuarioid', models.IntegerField()),
                ('autor', models.CharField(default='', max_length=40)),
                ('imagen', models.CharField(default='', max_length=40)),
            ],
        ),
    ]
