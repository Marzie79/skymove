# Generated by Django 2.0.2 on 2020-09-23 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0005_newsletter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date'], 'verbose_name': 'News', 'verbose_name_plural': 'All News'},
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name': 'News Letter', 'verbose_name_plural': 'All News Letter'},
        ),
        migrations.AlterModelOptions(
            name='support',
            options={'ordering': ['-date'], 'verbose_name': 'Support', 'verbose_name_plural': 'Supports'},
        ),
    ]