# Generated by Django 3.2.9 on 2021-11-23 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='features',
            field=models.ManyToManyField(to='main_app.Feature'),
        ),
    ]
