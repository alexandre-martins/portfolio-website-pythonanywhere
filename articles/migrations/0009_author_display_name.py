# Generated by Django 2.2.4 on 2020-01-10 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_author_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='display_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
