# Generated by Django 5.0.3 on 2024-07-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_place_description_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='place',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='place',
            name='duration',
        ),
    ]
