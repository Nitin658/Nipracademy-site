# Generated by Django 4.2.10 on 2024-04-03 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nipracademy', '0023_delete_staffs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculties',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='media/faculties_img', verbose_name='faculties'),
        ),
    ]
