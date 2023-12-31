# Generated by Django 4.2.2 on 2023-06-21 22:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dance_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief description of the dance course', max_length=1000)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a dance style (e.g. Salsa)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dance_course_instance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular run of a specific dance course e.g. in one particular semester', primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('running', models.CharField(blank=True, choices=[('f', 'Finished'), ('o', 'Ongoing currently'), ('n', 'not yet started')], default='n', help_text='Is the course currently running, finished in the past or will start to be held in the future', max_length=1)),
                ('dance_course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.dance_course')),
                ('instructor', models.ManyToManyField(help_text='Select instructor(s) for this dance course instance', to='catalog.instructor')),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
        migrations.AddField(
            model_name='dance_course',
            name='style',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.style'),
        ),
    ]
