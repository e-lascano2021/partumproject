# Generated by Django 3.2.9 on 2021-11-23 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('difficulty', models.CharField(choices=[('E', 'Easy'), ('I', 'Intermediate'), ('D', 'Difficult')], default='I', max_length=1)),
            ],
        ),
    ]
