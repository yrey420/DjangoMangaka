# Generated by Django 3.1.3 on 2020-12-10 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0009_manga_portadamanga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='portadaManga',
            field=models.ImageField(blank=True, default='berserk.jpg', height_field=100, upload_to='', verbose_name='Imagen de portada', width_field=80),
        ),
    ]
