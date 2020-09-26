# Generated by Django 2.0.2 on 2020-09-26 13:41

from django.db import migrations, models
import tinymce.models
import utils.custom_fields


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0006_auto_20200923_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABoutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', utils.custom_fields.FarsiCharField(max_length=50, verbose_name='Title')),
                ('description', tinymce.models.HTMLField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='service/', verbose_name='Image')),
                ('counter', models.IntegerField(default=0, verbose_name='Counter')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'A Bout Us',
                'verbose_name_plural': 'All A Bout Us',
            },
        ),
    ]
