# Generated by Django 3.1.2 on 2020-10-10 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='videos',
            field=models.ManyToManyField(to='main_app.Video'),
        ),
    ]
