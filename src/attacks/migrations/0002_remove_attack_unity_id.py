# Generated by Django 2.2.4 on 2019-12-06 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attacks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attack',
            name='unity_id',
        ),
    ]