# Generated by Django 4.2 on 2024-02-22 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_blog_audience_blog_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='topic',
            new_name='blogIdea',
        ),
    ]
