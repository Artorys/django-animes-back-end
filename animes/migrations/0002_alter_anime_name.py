
# Generated by Django 4.1.5 on 2023-01-06 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0001_initial')
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='name',
            field=models.TextField(),
        ),
    ]
