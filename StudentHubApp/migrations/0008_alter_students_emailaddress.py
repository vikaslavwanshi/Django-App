# Generated by Django 5.0.3 on 2024-03-19 04:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("StudentHubApp", "0007_students_courseenrolled"),
    ]

    operations = [
        migrations.AlterField(
            model_name="students",
            name="emailAddress",
            field=models.EmailField(max_length=255),
        ),
    ]
