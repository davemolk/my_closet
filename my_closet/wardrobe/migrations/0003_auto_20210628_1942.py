# Generated by Django 3.2.3 on 2021-06-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0002_auto_20210628_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottom',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='dress',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='outerwear',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='top',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
