# Generated by Django 3.1.1 on 2021-04-07 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_thumbnail',
            field=models.ImageField(default='', upload_to='thumbnails/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
