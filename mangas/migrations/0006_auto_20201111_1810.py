# Generated by Django 3.1.3 on 2020-11-11 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0005_auto_20201111_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='imageM',
            field=models.ImageField(blank=True, default='/berserk.jpg', null=True, upload_to='', verbose_name='Imagen'),
        ),
    ]