# Generated by Django 3.1.1 on 2021-04-03 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('listings', '0004_auto_20210401_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(default='Awadh Construction', on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor'),
        ),
    ]
