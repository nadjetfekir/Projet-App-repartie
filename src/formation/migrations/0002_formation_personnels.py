# Generated by Django 3.2.9 on 2021-12-06 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0002_auto_20211119_1908'),
        ('formation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='personnels',
            field=models.ManyToManyField(to='personnel.Personnel'),
        ),
    ]