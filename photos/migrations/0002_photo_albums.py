# Generated by Django 2.0.5 on 2018-05-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='albums',
            field=models.ManyToManyField(to='photos.Album'),
        ),
    ]
