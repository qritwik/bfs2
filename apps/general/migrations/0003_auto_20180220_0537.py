# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-20 05:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("general", "0002_user_ug")]

    operations = [
        migrations.AlterField(
            model_name="teaches",
            name="sem",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="general.Semester"
            ),
        )
    ]
