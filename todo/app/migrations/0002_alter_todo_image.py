# Generated by Django 4.1.3 on 2022-12-07 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='image',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='picture'),
        ),
    ]
