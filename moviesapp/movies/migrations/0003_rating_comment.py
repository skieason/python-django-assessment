# Generated by Django 3.0.6 on 2020-06-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200609_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
