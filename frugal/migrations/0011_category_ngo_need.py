# Generated by Django 2.1.3 on 2018-12-05 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frugal', '0010_auto_20181205_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ngo_Need',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_Name', models.CharField(max_length=20)),
                ('Count', models.IntegerField()),
                ('Detail', models.CharField(max_length=1000)),
                ('Photo', models.ImageField(upload_to='frugal/static/frugal/images/Need')),
                ('Status', models.CharField(choices=[('A', 'Activated'), ('D', 'Deactivated')], default='A', max_length=1)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frugal.Category')),
                ('NGO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frugal.NGO')),
            ],
        ),
    ]
