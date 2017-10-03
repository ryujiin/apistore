# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('utiles', '__first__'),
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuentaMayorista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('deuda_mes', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('acuenta_mes', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('venta_mes', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('mayorista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Mayorista')),
            ],
        ),
        migrations.CreateModel(
            name='Ingresos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('monto', models.DecimalField(blank=True, decimal_places=2, help_text=b'La cantidad de dinero que ingreso', max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PagoMayorista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('monto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('mayorista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Mayorista')),
            ],
        ),
        migrations.CreateModel(
            name='SerieTallas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SerieVentaMayorista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField()),
                ('precio', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('mayorista', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Mayorista')),
            ],
        ),
        migrations.CreateModel(
            name='VentaMayorista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cantidad_docenas', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('mayorista', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Cliente_mayorista', to='cliente.Mayorista')),
                ('producto', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Producto')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidad.SerieVentaMayorista')),
            ],
        ),
        migrations.AddField(
            model_name='serietallas',
            name='serie_venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tallas', to='contabilidad.SerieVentaMayorista'),
        ),
        migrations.AddField(
            model_name='serietallas',
            name='talla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utiles.Talla'),
        ),
    ]
