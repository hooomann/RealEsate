# Generated by Django 3.1.1 on 2021-03-24 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='intention',
            field=models.CharField(default='Sale', max_length=4),
        ),
    ]
