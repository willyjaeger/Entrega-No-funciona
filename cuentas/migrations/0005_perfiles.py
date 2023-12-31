# Generated by Django 4.2.3 on 2023-08-31 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0004_usuario_nombreusuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.CharField(default='', max_length=40)),
                ('nombre', models.CharField(default='', max_length=40)),
                ('descripcion', models.CharField(default='', max_length=100)),
                ('usuarioid', models.IntegerField()),
                ('paginaweb', models.CharField(default='', max_length=40)),
                ('email', models.EmailField(default='', max_length=40, null=True)),
                ('contraseña', models.CharField(max_length=40)),
            ],
        ),
    ]
