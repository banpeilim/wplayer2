# Generated by Django 4.0.4 on 2022-05-22 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='destination',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='flight',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='gate',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
