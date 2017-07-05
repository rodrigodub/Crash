# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Computer', '0005_auto_20170624_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccconnection',
            name='battery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Computer.CCBattery'),
        ),
        migrations.AddField(
            model_name='ccconnection',
            name='batteryfield',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ccconnection',
            name='transistor2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connection_to', to='Computer.CCTransistor'),
        ),
        migrations.AlterField(
            model_name='ccconnection',
            name='transistor2field',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]