# Generated by Django 3.0.9 on 2020-08-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read_cnt',
            field=models.IntegerField(default=0),
        ),
    ]