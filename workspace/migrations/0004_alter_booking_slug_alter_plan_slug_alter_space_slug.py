# Generated by Django 4.0.4 on 2022-05-10 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0003_booking_slug_plan_slug_space_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='space',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
