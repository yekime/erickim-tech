# Generated by Django 4.0.6 on 2022-07-14 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_remove_projectinfo_github_projectinfo_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='github',
            field=models.URLField(blank=True),
        ),
    ]
