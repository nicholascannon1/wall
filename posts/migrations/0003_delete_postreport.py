# Generated by Django 3.0.8 on 2020-07-12 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_edited'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostReport',
        ),
    ]
