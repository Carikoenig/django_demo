# Generated by Django 4.2.2 on 2023-06-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a language (e.g. French)', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='style',
            name='partner_needed',
            field=models.CharField(blank=True, choices=[('s', 'solo dance'), ('p', 'partnered')], default='p', help_text='enter whether this is a pair dance with partner (e.g. Ballroom) or a solo dance (e.g. Hip hop)', max_length=1),
        ),
        migrations.AddField(
            model_name='instructor',
            name='speaks_language',
            field=models.ManyToManyField(help_text='Select language(s) the instructor can teach in', to='catalog.language'),
        ),
    ]
