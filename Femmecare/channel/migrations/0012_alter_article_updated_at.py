# Generated by Django 4.2.4 on 2024-03-31 03:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0011_alter_article_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 31, 9, 33, 46, 867278)),
        ),
    ]
