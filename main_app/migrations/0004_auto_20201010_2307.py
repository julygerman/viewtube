# Generated by Django 3.1.2 on 2020-10-10 23:07

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_user_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
