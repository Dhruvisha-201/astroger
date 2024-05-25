# Generated by Django 4.1.6 on 2023-03-14 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astroakshat', '0002_remove_sign_sign_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='astro_admin',
            name='IsDeleted',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='daily_articals',
            name='IsDeleted',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='daily_horoscope',
            name='IsDeleted',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kundli',
            name='IsDeleted',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='panchag',
            name='IsDeleted',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
