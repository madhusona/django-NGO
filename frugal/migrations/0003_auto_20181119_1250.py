# Generated by Django 2.1.3 on 2018-11-19 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frugal', '0002_auto_20181116_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='Website',
            field=models.CharField(blank=True, help_text='Optional. Maximum 30 Characters', max_length=30, null=True),
        ),
    ]