# Generated by Django 4.0.1 on 2022-09-12 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('untersetzerBroker', '0004_quickaccesstemplatefood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempcoastergroup',
            name='identifier',
        ),
    ]
