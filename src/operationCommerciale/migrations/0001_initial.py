# Generated by Django 3.2.9 on 2021-12-06 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personnel', '0002_auto_20211119_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperationCommerciale',
            fields=[
                ('identifiant', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('achat', 'Achat'), ('vente', 'Vente')], max_length=14)),
                ('margeDegagee', models.FloatField()),
                ('nombreKm', models.FloatField()),
                ('motCleResponsable', models.CharField(max_length=255)),
                ('motCleClient', models.CharField(max_length=255)),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personnel.personnel')),
            ],
        ),
    ]
