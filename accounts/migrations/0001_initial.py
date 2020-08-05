# Generated by Django 3.1 on 2020-08-05 13:24

from django.db import migrations, models
import utils.custom_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nationality', models.CharField(max_length=10, unique=True)),
                ('first_name', utils.custom_fields.FarsiCharField(max_length=30)),
                ('last_name', utils.custom_fields.FarsiCharField(max_length=30)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('company_name', utils.custom_fields.FarsiCharField(blank=True, max_length=40, null=True)),
                ('validation', models.CharField(blank=True, max_length=8, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['nationality'],
            },
        ),
    ]
