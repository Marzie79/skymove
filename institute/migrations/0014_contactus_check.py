# Generated by Django 2.0.2 on 2020-09-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0013_auto_20200926_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='check',
            field=models.BooleanField(default=False, verbose_name='Check'),
        ),
    ]