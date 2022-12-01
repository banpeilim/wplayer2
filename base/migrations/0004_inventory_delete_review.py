# Generated by Django 4.0.4 on 2022-09-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storeid', models.CharField(blank=True, max_length=200, null=True)),
                ('productid', models.CharField(blank=True, max_length=200, null=True)),
                ('udpip', models.CharField(blank=True, max_length=200, null=True)),
                ('stock', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
