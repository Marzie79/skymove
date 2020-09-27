# Generated by Django 2.0.2 on 2020-09-27 12:47

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_socialnetwork_facebook'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutushome',
            options={'ordering': ['-id'], 'verbose_name': 'A bout us in home', 'verbose_name_plural': 'All a bout us in home'},
        ),
        migrations.AlterModelOptions(
            name='homevideo',
            options={'ordering': ['-id'], 'verbose_name': 'Video', 'verbose_name_plural': 'Video in home'},
        ),
        migrations.RemoveField(
            model_name='aboutushome',
            name='date',
        ),
        migrations.RemoveField(
            model_name='homevideo',
            name='date',
        ),
        migrations.AddField(
            model_name='aboutushome',
            name='active',
            field=models.BooleanField(default=True, help_text='if you set this field true this information is shown in about us in home page', verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='homevideo',
            name='active',
            field=models.BooleanField(default=True, help_text='if you set this field true this video is shown in home page', verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='active',
            field=models.BooleanField(default=True, help_text='if you set this field true this information is shown in footer of pages', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='enter phone number with country code like : +98... ', max_length=128, region=None, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='whats_app_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='enter phone number with country code like : +98... ', max_length=128, null=True, region=None, verbose_name='Whats app phone number'),
        ),
    ]
