# Generated by Django 3.1.3 on 2020-11-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='imagenM',
        ),
        migrations.AddField(
            model_name='manga',
            name='imageM',
            field=models.ImageField(default=2, upload_to='mediafiles/', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
