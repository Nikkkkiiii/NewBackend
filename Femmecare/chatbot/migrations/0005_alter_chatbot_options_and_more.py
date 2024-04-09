# Generated by Django 4.2.4 on 2024-04-08 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatbot', '0004_alter_chatbot_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatbot',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='chatbot',
            old_name='dateTime',
            new_name='created',
        ),
        migrations.AlterField(
            model_name='chatbot',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatbot',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]