# Generated by Django 5.0.3 on 2024-07-07 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_difficulty_duration_remove_place_difficulty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='difficulty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.difficulty'),
        ),
        migrations.AddField(
            model_name='place',
            name='duration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.duration'),
        ),
    ]
