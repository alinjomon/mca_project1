# Generated by Django 3.2.20 on 2023-10-19 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_dress_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.CharField(default='A', max_length=500),
        ),
    ]
