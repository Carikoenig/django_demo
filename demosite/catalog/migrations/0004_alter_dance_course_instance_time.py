# Generated by Django 4.2.2 on 2023-06-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_dance_course_instance_day_dance_course_instance_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dance_course_instance',
            name='time',
            field=models.CharField(blank=True, max_length=14),
        ),
    ]
