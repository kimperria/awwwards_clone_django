# Generated by Django 4.0.3 on 2022-04-09 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_profile_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]