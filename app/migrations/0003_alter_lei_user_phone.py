# Generated by Django 4.0.5 on 2022-06-19 06:06

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_parent_companies_from_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lei_user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]