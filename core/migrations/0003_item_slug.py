# Generated by Django 2.2 on 2022-05-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220518_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test product'),
            preserve_default=False,
        ),
    ]