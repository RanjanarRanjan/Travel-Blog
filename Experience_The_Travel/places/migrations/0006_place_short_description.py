# Generated by Django 5.0.3 on 2024-07-03 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_place_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='short_description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
