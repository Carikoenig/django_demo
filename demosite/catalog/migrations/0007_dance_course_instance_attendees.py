# Generated by Django 4.2.2 on 2023-06-24 17:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0006_alter_instructor_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='dance_course_instance',
            name='attendees',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
