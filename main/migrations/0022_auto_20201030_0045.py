# Generated by Django 3.1.2 on 2020-10-30 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20201029_1659'),
    ]

    operations = [
        migrations.DeleteModel(
            name='img',
        ),
        migrations.AddField(
            model_name='exam_info',
            name='sort',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='user_info',
            name='sort',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='user_score',
            name='exam_num',
            field=models.IntegerField(default=0),
        ),
    ]