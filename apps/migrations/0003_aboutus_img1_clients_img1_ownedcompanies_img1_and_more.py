# Generated by Django 4.0.3 on 2022-03-25 01:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_certificates_img1'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='img1',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='apps/static/images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clients',
            name='img1',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='apps/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ownedcompanies',
            name='img1',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='apps/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='desc',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='footer',
            name='phone1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='footer',
            name='phone2',
            field=models.CharField(max_length=50),
        ),
    ]