# Generated by Django 4.1 on 2022-08-21 10:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post_image_app', '0003_alter_post_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
