# Generated by Django 3.2.9 on 2021-12-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('identifiant', models.IntegerField(default=0, primary_key=True, serialize=False)),
            ],
        ),
    ]