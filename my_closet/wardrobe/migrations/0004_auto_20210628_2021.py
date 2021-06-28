# Generated by Django 3.2.3 on 2021-06-28 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0003_auto_20210628_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('sell', models.BooleanField(default=False)),
                ('tag', models.ManyToManyField(to='wardrobe.Tag')),
            ],
        ),
        migrations.RemoveField(
            model_name='dress',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='outerwear',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='top',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='outfit',
            name='bottom',
        ),
        migrations.RemoveField(
            model_name='outfit',
            name='dress',
        ),
        migrations.RemoveField(
            model_name='outfit',
            name='outerwear',
        ),
        migrations.RemoveField(
            model_name='outfit',
            name='shoe',
        ),
        migrations.RemoveField(
            model_name='outfit',
            name='top',
        ),
        migrations.DeleteModel(
            name='Bottom',
        ),
        migrations.DeleteModel(
            name='Dress',
        ),
        migrations.DeleteModel(
            name='Outerwear',
        ),
        migrations.DeleteModel(
            name='Shoe',
        ),
        migrations.DeleteModel(
            name='Top',
        ),
        migrations.AddField(
            model_name='outfit',
            name='clothing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outfits', to='wardrobe.clothing'),
        ),
    ]
