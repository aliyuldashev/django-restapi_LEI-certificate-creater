# Generated by Django 4.0.5 on 2022-06-19 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_lei_user_billing_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lei_user',
            name='total_money',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
