# Generated by Django 4.2.4 on 2024-04-08 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0017_alter_article_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 8, 23, 15, 47, 936877)),
        ),
    ]
