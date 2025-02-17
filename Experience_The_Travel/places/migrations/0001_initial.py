# Generated by Django 5.0.3 on 2024-07-03 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('destination_type', models.CharField(choices=[('beach', 'Beach'), ('mountain', 'Mountain'), ('city', 'City'), ('forest', 'Forest')], max_length=50)),
                ('duration', models.CharField(choices=[('5 days', '5 days'), ('10 days', '10 days'), ('15 days', '15 days'), ('1 week', '1 week')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('moderate', 'Moderate'), ('hard', 'Hard')], max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
