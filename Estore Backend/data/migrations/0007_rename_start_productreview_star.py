# Generated by Django 4.1.7 on 2023-03-29 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0006_productreview"),
    ]

    operations = [
        migrations.RenameField(
            model_name="productreview",
            old_name="start",
            new_name="star",
        ),
    ]