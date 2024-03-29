# Generated by Django 2.1.7 on 2019-04-05 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Satisfaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitter', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('date', models.DateField()),
                ('score', models.IntegerField(null=True)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
