# Generated by Django 3.2.3 on 2021-06-28 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottom',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='dress',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='outerwear',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='outfit',
            name='bottom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outfits', to='wardrobe.bottom'),
        ),
        migrations.AddField(
            model_name='outfit',
            name='dress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outfits', to='wardrobe.dress'),
        ),
        migrations.AddField(
            model_name='outfit',
            name='outerwear',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outfits', to='wardrobe.outerwear'),
        ),
        migrations.AddField(
            model_name='outfit',
            name='shoe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outfits', to='wardrobe.shoe'),
        ),
        migrations.AddField(
            model_name='outfit',
            name='top',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outfits', to='wardrobe.top'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='top',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
