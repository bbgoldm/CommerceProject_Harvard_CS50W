# Generated by Django 3.2.6 on 2021-08-30 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing_fake'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='fake',
        ),
    ]
