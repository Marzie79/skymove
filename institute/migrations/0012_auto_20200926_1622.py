# Generated by Django 2.0.2 on 2020-09-26 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0011_delete_newsletter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'ordering': ['-date'], 'verbose_name': 'A bout us', 'verbose_name_plural': "All a bout us page's data"},
        ),
    ]
