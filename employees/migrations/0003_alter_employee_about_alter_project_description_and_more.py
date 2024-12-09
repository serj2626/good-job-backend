# Generated by Django 5.1 on 2024-12-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0002_employee_status_alter_resume_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="about",
            field=models.TextField(blank=True, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="resume",
            name="about",
            field=models.TextField(blank=True, null=True, verbose_name="О себе"),
        ),
    ]
