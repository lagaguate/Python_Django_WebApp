# Generated by Django 4.1 on 2023-07-18 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0003_contacto_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='imagen',
            field=models.ImageField(help_text='Test Help', upload_to='contacto'),
        ),
    ]
