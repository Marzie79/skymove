# Generated by Django 2.0.2 on 2020-09-05 15:14

from django.db import migrations
import utils.custom_fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200905_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=utils.custom_fields.FarsiCharField(error_messages={'max_length': 'This email has already been registered.'}, max_length=30, verbose_name='First name'),
        ),
    ]