# Generated by Django 5.0.3 on 2024-03-24 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("affirmations", "0004_alter_textaffirmations_recording"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="textaffirmations",
            name="recording",
        ),
    ]
