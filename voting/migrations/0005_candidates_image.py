# Generated by Django 4.2.7 on 2023-11-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_rename_description_candidates_manifesto'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]