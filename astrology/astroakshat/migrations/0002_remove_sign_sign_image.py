# Generated by Django 4.1.6 on 2023-03-14 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('astroakshat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sign',
            name='sign_image',
        ),
    ]
