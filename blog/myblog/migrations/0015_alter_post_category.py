# Generated by Django 4.2.7 on 2023-12-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0014_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('coding', 'Coding'), ('music', 'Music'), ('art', 'Art'), ('food', 'Food'), ('makeup', 'Makeup')], default='coding', max_length=255),
        ),
    ]
