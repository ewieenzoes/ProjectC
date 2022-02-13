# Generated by Django 4.0.1 on 2022-02-13 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('untersetzerBroker', '0002_untersetzer_identifier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=200)),
                ('coasters', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Beverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('edition', models.CharField(max_length=200)),
                ('coaster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beverage', to='untersetzerBroker.untersetzer')),
            ],
        ),
        migrations.AlterField(
            model_name='untersetzer',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table', to='untersetzerBroker.table'),
        ),
    ]