# Generated by Django 4.2.5 on 2023-10-31 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('tipo_de_archivo', models.CharField(max_length=8)),
                ('articulo', models.IntegerField()),
                ('metodo_de_pago', models.CharField(max_length=7)),
            ],
        ),
    ]
