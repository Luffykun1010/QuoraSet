# Generated by Django 4.2.6 on 2023-10-27 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quora_page', '0002_alter_posts_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
