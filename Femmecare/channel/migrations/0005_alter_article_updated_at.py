# Generated by Django 4.2.4 on 2024-03-27 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0004_alter_article_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 23, 30, 32, 563552)),
        ),
    ]
