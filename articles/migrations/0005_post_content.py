# Generated by Django 2.2.4 on 2020-01-05 18:18

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20191215_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='test'),
            preserve_default=False,
        ),
    ]
