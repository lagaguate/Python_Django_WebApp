# Generated by Django 4.1 on 2023-06-29 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(null=True, upload_to='blog'),
        ),
    ]