# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-18 16:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("general", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        choices=[
                            ("Excellent", "Excellent"),
                            ("Good", "Good"),
                            ("Satisfactory", "Satisfactory"),
                            ("Poor", "Poor"),
                            ("Very Poor", "Very Poor"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeedbackForm",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="Form Title")),
                (
                    "description",
                    models.CharField(max_length=250, verbose_name="Form Description"),
                ),
                (
                    "code",
                    models.CharField(
                        help_text="Mandatory to enter two charachters",
                        max_length=2,
                        verbose_name="Form Code",
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        help_text="Type of user that is receiving the feedback for this form",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="form",
                        to="general.UserType",
                    ),
                ),
                (
                    "user_type",
                    models.ManyToManyField(
                        help_text="Type of user that is allowed to give the feedback for this form",
                        to="general.UserType",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Question")),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="feedback.FeedbackForm",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="feedback.Question"
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="recipient",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="teacher",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="general.Teaches",
            ),
        ),
    ]
