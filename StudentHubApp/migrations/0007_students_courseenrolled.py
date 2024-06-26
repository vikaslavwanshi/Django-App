# Generated by Django 5.0.3 on 2024-03-16 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("StudentHubApp", "0006_remove_students_courseenrolled"),
    ]

    operations = [
        migrations.AddField(
            model_name="students",
            name="courseEnrolled",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="StudentHubApp.courses",
            ),
            preserve_default=False,
        ),
    ]
