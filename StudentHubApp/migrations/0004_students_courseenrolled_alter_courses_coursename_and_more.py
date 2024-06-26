# Generated by Django 5.0.3 on 2024-03-14 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("StudentHubApp", "0003_rename_capacity_courses_capacity"),
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
        ),
        migrations.AlterField(
            model_name="courses",
            name="courseName",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="courses",
            name="nameOfCourseCordinator",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="students",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="students",
            name="studentId",
            field=models.IntegerField(unique=True),
        ),
    ]
