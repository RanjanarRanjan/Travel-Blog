# Generated by Django 5.0.3 on 2024-07-04 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_place_destination_type_alter_place_difficulty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Typology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='typologies',
            field=models.ManyToManyField(related_name='places', to='places.typology'),
        ),
    ]
