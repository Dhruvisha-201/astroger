# Generated by Django 4.1.6 on 2023-09-17 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('astroakshat', '0011_remove_lalkitab_clientlog_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_birth_journal',
            name='birth_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='astroakshat.birth'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='create_kundli_dosh',
            name='kundli_dosh_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='astroakshat.kundli_dosh'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='create_manglik',
            name='manglik_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='astroakshat.manglik'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='create_match',
            name='match_matching_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='astroakshat.match_matching'),
            preserve_default=False,
        ),
    ]
