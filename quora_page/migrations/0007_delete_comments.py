# Generated by Django 4.2.6 on 2023-10-28 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quora_page', '0006_remove_comments_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
