# Generated by Django 2.1.2 on 2018-11-15 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0007_card_cardmanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CardManager',
        ),
        migrations.AddField(
            model_name='card',
            name='default',
            field=models.BooleanField(default=True),
        ),
    ]