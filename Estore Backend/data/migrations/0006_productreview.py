# Generated by Django 4.1.7 on 2023-03-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0005_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductReview",
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
                ("email", models.EmailField(max_length=254)),
                ("review", models.TextField()),
                ("slug", models.TextField()),
                ("start", models.IntegerField(default=1)),
            ],
        ),
    ]