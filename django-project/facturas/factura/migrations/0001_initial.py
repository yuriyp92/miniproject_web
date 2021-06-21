# Generated by Django 3.2.4 on 2021-06-19 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=0)),
                ('anio', models.DateField()),
                ('fecha_emision', models.DateField()),
                ('cliente_nombre', models.CharField(max_length=100)),
                ('cliente_direccion', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='LineaFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_unitario', models.FloatField(default=0)),
                ('unidades', models.IntegerField(default=1)),
                ('nombre_producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='factura.factura')),
            ],
        ),
    ]