# Generated by Django 2.2.2 on 2020-06-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='email',
            field=models.CharField(default=0, max_length=100, primary_key=True, serialize=False),
        ),
    ]
