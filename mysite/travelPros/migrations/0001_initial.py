# Generated by Django 4.2.11 on 2024-05-04 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Traveler",
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
                ("name", models.CharField(max_length=100)),
                ("departure_date", models.CharField(max_length=100)),
                ("arrival_date", models.CharField(max_length=100)),
            ],
        ),
    ]
