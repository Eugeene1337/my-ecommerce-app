# Generated by Django 2.2 on 2022-05-20 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Natus suscripit modi sapiente illo soluta odit voluptates, quibusdam officia. Nesque quibusdam quas a quis porro? Molestias illo neque eum in laborum.'),
            preserve_default=False,
        ),
    ]
