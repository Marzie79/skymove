# Generated by Django 2.0.2 on 2020-09-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0020_auto_20200927_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='active',
            field=models.BooleanField(default=True, help_text='if you set this field true this information is shown in support of about us page', verbose_name='Active'),
        ),
    ]
