# Generated by Django 2.0.2 on 2020-09-27 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0015_auto_20200926_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
