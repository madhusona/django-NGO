# Generated by Django 2.1.3 on 2018-12-07 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frugal', '0003_ngo_need'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Credit_Point',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
