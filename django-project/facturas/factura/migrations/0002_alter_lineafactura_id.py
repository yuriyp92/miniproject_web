# Generated by Django 3.2.4 on 2021-06-20 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineafactura',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
