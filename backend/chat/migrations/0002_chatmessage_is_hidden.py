# Generated by Django 5.1.1 on 2025-05-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatmessage",
            name="is_hidden",
            field=models.BooleanField(default=False, verbose_name="是否隐藏"),
        ),
    ]
