# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("django_chatterbot", "0010_statement_text")]

    operations = [
        migrations.AlterField(
            model_name="statement",
            name="extra_data",
            field=models.CharField(blank=True, max_length=500),
        )
    ]
