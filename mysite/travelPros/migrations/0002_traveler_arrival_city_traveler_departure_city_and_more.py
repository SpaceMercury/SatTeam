# Generated by Django 4.2.11 on 2024-05-05 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travelPros", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="traveler",
            name="arrival_city",
            field=models.CharField(default="Paris", max_length=100),
        ),
        migrations.AddField(
            model_name="traveler",
            name="departure_city",
            field=models.CharField(default="Barcelona", max_length=100),
        ),
        migrations.AddField(
            model_name="traveler",
            name="number_of_days",
            field=models.IntegerField(default=1),
        ),
    ]
