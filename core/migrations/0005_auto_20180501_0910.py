# Generated by Django 2.0.4 on 2018-05-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cronsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultfromparsing',
            name='h1',
            field=models.TextField(blank=True),
        ),
    ]
