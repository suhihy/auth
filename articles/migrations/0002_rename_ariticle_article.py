# Generated by Django 5.0.7 on 2024-08-06 05:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ariticle',
            new_name='Article',
        ),
    ]
