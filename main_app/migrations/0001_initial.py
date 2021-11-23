# Generated by Django 3.2.9 on 2021-11-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('description', models.TextField(max_length=350)),
                ('progress', models.CharField(choices=[('N', 'Not Started'), ('P', 'In Progress'), ('C', 'Completed')], default='N', max_length=1)),
            ],
        ),
    ]
