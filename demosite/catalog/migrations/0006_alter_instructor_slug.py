# Generated by Django 4.2.2 on 2023-06-23 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_instructor_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
