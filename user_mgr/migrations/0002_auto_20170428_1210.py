# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgr', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address'},
        ),
        migrations.AlterModelOptions(
            name='friendlist',
            options={'verbose_name_plural': 'FriendList'},
        ),
        migrations.AlterModelOptions(
            name='useraccount',
            options={'verbose_name_plural': 'UserAccount'},
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='status',
            field=models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married'), ('others', 'Others')], max_length=10, null=True),
        ),
    ]