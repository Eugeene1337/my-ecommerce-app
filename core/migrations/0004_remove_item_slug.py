# Generated by Django 2.2 on 2022-05-20 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='slug',
        ),
    ]