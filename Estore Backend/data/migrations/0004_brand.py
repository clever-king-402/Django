# Generated by Django 4.1.7 on 2023-03-27 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0003_ad"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
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
                ("name", models.CharField(max_length=400)),
                ("image", models.ImageField(upload_to="media")),
            ],
        ),
    ]
