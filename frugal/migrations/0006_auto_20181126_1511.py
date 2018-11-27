# Generated by Django 2.1.3 on 2018-11-26 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frugal', '0005_auto_20181122_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='Latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='ngo',
            name='Longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=13, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='Address',
            field=models.CharField(help_text='Door No and Street. Maximum 200 Characters', max_length=200),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='City',
            field=models.CharField(help_text='Maximum 50 Characters', max_length=50),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='Contact_Person',
            field=models.CharField(help_text='Maximum 50 Characters', max_length=50),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='Email_id',
            field=models.CharField(help_text='Maximum 50 Characters', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='Mobile_no',
            field=models.CharField(help_text='Should be 10 Characters', max_length=10),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='Organization_Name',
            field=models.CharField(help_text='Maximum 200 Characters', max_length=200),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='Pincode',
            field=models.CharField(help_text='Should be 6 Characters', max_length=6),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='Website',
            field=models.CharField(blank=True, help_text='Maximum 30 Characters', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ngo_profile',
            name='Cover_Photo',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='ngo_registration',
            name='Recognized_Body',
            field=models.CharField(max_length=100),
        ),
    ]