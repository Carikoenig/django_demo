# Generated by Django 4.2.2 on 2023-06-22 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language_style_partner_needed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dance_course_instance',
            name='day',
            field=models.CharField(blank=True, choices=[('mo', 'Monday'), ('tu', 'Tuesday'), ('we', 'Wednesday'), ('th', 'Thursday'), ('fr', 'Friday'), ('sa', 'Saturday'), ('su', 'Sunday')], default='mo', help_text='On which day is the course?', max_length=2),
        ),
        migrations.AddField(
            model_name='dance_course_instance',
            name='time',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
