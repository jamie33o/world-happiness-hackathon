# Generated by Django 3.2.25 on 2024-03-23 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("affirmations", "0002_textaffirmations"),
    ]

    operations = [
        migrations.RenameField(
            model_name="textaffirmations",
            old_name="messsage",
            new_name="message",
        ),
    ]
