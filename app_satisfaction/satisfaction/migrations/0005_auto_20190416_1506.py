# Generated by Django 2.1.7 on 2019-04-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satisfaction', '0004_fruit'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='score_calendar',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='score',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]