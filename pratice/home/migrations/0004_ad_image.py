# Generated by Django 5.0.1 on 2024-02-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
