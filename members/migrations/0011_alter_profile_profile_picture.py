# Generated by Django 4.0.3 on 2022-04-09 23:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dbgbail9r/image/upload/v1649544556/profile_image_kfrlhw.png', max_length=255, verbose_name='images/'),
        ),
    ]