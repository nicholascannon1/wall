# Generated by Django 3.0.8 on 2020-07-12 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited',
            field=models.BooleanField(default=False),
        ),
    ]
