# Generated by Django 5.0.7 on 2024-07-16 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxAllApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]
