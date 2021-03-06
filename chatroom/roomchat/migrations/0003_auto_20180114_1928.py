# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-14 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roomchat', '0002_remove_roomchat_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.UserProfile'),
        ),
        migrations.AlterField(
            model_name='roomchat',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='owned_rooms', to='userprofile.UserProfile'),
        ),
    ]
