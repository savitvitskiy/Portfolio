# Generated by Django 4.2.3 on 2023-11-10 01:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.FileField(blank=True, upload_to="project_images/"),
        ),
    ]
