# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-20 00:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20170824_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='variacion',
        ),
        migrations.RemoveField(
            model_name='comentarioimagen',
            name='comentario',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.DeleteModel(
            name='ComentarioImagen',
        ),
    ]