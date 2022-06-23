# Generated by Django 4.0.5 on 2022-06-23 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amechanic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='location_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.ManyToManyField(to='amechanic.location'),
        ),
    ]