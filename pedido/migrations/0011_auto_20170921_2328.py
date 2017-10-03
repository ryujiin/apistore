# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-21 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0010_auto_20170921_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado_pedido',
            field=models.CharField(choices=[(b'autenticado', '<b>Autenticado</b> - Usted se encuentra idenficado en la plataforma'), (b'metodo_envio', 'Metodo de Envio - Ya selecciono el metodo de envio, esperando metodo de pago'), (b'metodo_pago', 'Metodo de Pago - Ya selecciono el metodo de pago'), (b'esperando_pago', 'Esperando Pago - Ya selecciono el metodo de pago, pero aun no se realiza el pago'), (b'pagado', 'Pagado - El pago se realizo correctamente, espere el envio del producto'), (b'error_pago', 'Error en Pago - Ocurrio un error al pagar'), (b'enviado', 'Enviado - El producto fue enviado'), (b'devuelto', 'Devuelto - El producto fue devuelto'), (b'fucionado', 'Fusionado - Este Pedido se Fusiono con otro pedido')], default=b'autenticado', max_length=120),
        ),
    ]
