# Generated by Django 2.1.7 on 2019-04-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satisfaction', '0002_auto_20190405_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='submitter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
