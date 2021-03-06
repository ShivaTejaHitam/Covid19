# Generated by Django 2.2.2 on 2020-06-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esic', '0003_auto_20200625_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='iw_occupied',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Occupied Isolation Wards'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='iw_vacant',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Vacant Isolation Wards'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='total_iw',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total Isolation Wards'),
        ),
    ]
