# Generated by Django 4.2.7 on 2023-12-04 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pinterest_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]
