# Generated by Django 4.0.5 on 2022-06-19 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_lei_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='lei_user',
            name='billing_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='billing', to='app.billing_data'),
        ),
        migrations.AlterField(
            model_name='lei_user',
            name='reason_unprovide',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='lei_user',
            name='total_money',
            field=models.BigIntegerField(blank=True),
        ),
    ]
