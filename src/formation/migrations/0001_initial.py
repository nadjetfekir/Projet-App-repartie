# Generated by Django 3.2.9 on 2021-12-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomFormation', models.CharField(blank=True, max_length=255)),
                ('sujet', models.TextField()),
                ('date', models.DateTimeField()),
                ('pourcentageEngagement', models.FloatField()),
                ('pourcentageSatisfaction', models.FloatField()),
                ('MotCleFormateur', models.CharField(max_length=255)),
                ('MotClePersonnel', models.CharField(max_length=255)),
            ],
        ),
    ]
