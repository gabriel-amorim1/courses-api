# Generated by Django 3.2.9 on 2021-11-22 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_courses_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='quantity_of_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
