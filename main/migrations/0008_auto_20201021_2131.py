# Generated by Django 3.1.2 on 2020-10-21 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201021_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='first_name',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='user_info',
            name='last_name',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='user_grade',
            field=models.IntegerField(default=0),
        ),
    ]
