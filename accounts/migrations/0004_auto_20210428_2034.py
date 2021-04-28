# Generated by Django 3.2 on 2021-04-28 20:34

from django.db import migrations
import utils.custom_fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201201_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company_name_persian',
            field=utils.custom_fields.FarsiCharField(blank=True, max_length=40, null=True, verbose_name='Company name Persian'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=utils.custom_fields.FarsiCharField(max_length=30, verbose_name='Last name Persian'),
        ),
    ]
