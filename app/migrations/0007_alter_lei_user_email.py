# Generated by Django 4.0.5 on 2022-06-23 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_lei_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lei_user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
