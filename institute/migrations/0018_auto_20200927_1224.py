# Generated by Django 2.0.2 on 2020-09-27 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0017_auto_20200927_1209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='support',
            options={'ordering': ['-id'], 'verbose_name': 'Support address', 'verbose_name_plural': 'Support addresses'},
        ),
        migrations.RemoveField(
            model_name='support',
            name='date',
        ),
        migrations.AddField(
            model_name='support',
            name='active',
            field=models.BooleanField(default=True, help_text='if you set this field true this information is shown in about us page', verbose_name='Active'),
        ),
    ]