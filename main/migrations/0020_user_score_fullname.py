# Generated by Django 3.1.2 on 2020-10-27 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20201027_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_score',
            name='FullName',
            field=models.CharField(default='', max_length=200),
        ),
    ]