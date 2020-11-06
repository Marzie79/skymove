# Generated by Django 3.1.2 on 2020-11-06 09:32

from django.db import migrations, models
import phonenumber_field.modelfields
import utils.custom_fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutushome',
            options={'ordering': ['-id'], 'verbose_name': 'About us in home', 'verbose_name_plural': 'About us in home'},
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'ordering': ['-id'], 'verbose_name': 'News letter', 'verbose_name_plural': 'News letter'},
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='address',
            field=utils.custom_fields.FarsiTextField(blank=True, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='map',
            field=models.TextField(blank=True, help_text='Enter iframe tag from google map.', null=True, verbose_name='Map'),
        ),
        migrations.AlterField(
            model_name='aboutushome',
            name='active',
            field=models.BooleanField(default=True, help_text='If you set this field true this information is shown in about us in home page.', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='homevideo',
            name='active',
            field=models.BooleanField(default=True, help_text='If you set this field true this video is shown in home page.', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='homevideo',
            name='video',
            field=models.FileField(help_text='Size of video should be under 50 meg.', upload_to='video_uploaded/', verbose_name='Video'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='active',
            field=models.BooleanField(default=True, help_text='If you set this field true this information is shown in footer of pages.', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='whats_app_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Enter phone number with country code like : +98... ', max_length=128, null=True, region=None, verbose_name='Whats app phone number'),
        ),
    ]