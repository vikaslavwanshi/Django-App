# Generated by Django 5.0.1 on 2024-03-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Courses",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Capacity", models.IntegerField()),
                ("courseName", models.CharField(max_length=255)),
                ("nameOfCourseCordinator", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Students",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("emailAddress", models.CharField(max_length=255)),
                ("studentId", models.CharField(max_length=255)),
                ("dob", models.DateField(max_length=8)),
            ],
        ),
    ]
