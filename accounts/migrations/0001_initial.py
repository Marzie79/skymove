# Generated by Django 2.0.2 on 2020-08-31 12:02

import django.core.validators
from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields
import utils.custom_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nationality', django_countries.fields.CountryField(max_length=2, verbose_name='Nationality')),
                ('first_name', utils.custom_fields.FarsiCharField(max_length=30, verbose_name='First name')),
                ('last_name', utils.custom_fields.FarsiCharField(max_length=30, verbose_name='Last name')),
                ('email', models.EmailField(max_length=255, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='Email')),
                ('email_2', models.EmailField(blank=True, max_length=255, null=True, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='Email 2')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone number')),
                ('company_name', utils.custom_fields.FarsiCharField(blank=True, max_length=40, null=True, verbose_name='Company name')),
                ('validation', models.CharField(blank=True, max_length=6, null=True, verbose_name='Validation')),
                ('is_validate', models.BooleanField(default=False, verbose_name='Is validate')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is admin')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['nationality'],
            },
        ),
    ]
