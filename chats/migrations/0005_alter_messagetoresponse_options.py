# Generated by Django 5.1 on 2024-11-24 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chats", "0004_rename_message_messagetoresponse"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="messagetoresponse",
            options={
                "verbose_name": "Сообщение отклика",
                "verbose_name_plural": "Сообщения отклика",
            },
        ),
    ]