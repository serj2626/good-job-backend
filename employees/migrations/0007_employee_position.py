# Generated by Django 5.1 on 2024-11-21 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0006_remove_resume_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="position",
            field=models.CharField(
                blank=True, max_length=300, null=True, verbose_name="Должность"
            ),
        ),
    ]