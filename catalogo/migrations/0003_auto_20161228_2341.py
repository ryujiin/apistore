# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-28 23:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utiles', '0001_initial'),
        ('catalogo', '0002_producto_modelo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialproducto',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='materialproducto',
            name='costo',
        ),
        migrations.AddField(
            model_name='seccionproducto',
            name='cantidad',
            field=models.DecimalField(blank=True, decimal_places=2, help_text=b'La cantidad usada en este producto de este material', max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='seccionproducto',
            name='talla',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utiles.Talla'),
        ),
    ]
