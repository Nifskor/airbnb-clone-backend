# Generated by Django 4.1 on 2022-09-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medias", "0002_alter_photo_experience_alter_photo_room_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="file",
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name="video",
            name="file",
            field=models.URLField(),
        ),
    ]
