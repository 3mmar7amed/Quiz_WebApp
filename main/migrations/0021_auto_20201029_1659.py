# Generated by Django 3.1.2 on 2020-10-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_user_score_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question_text',
            field=models.TextField(),
        ),
    ]
