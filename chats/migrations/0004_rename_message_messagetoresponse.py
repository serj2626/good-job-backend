# Generated by Django 5.1 on 2024-11-24 10:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chats", "0003_delete_subscription"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Message",
            new_name="MessageToResponse",
        ),
    ]