# Generated by Django 5.1.2 on 2024-10-31 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_link', '0003_alter_url_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(default='6rv1U', max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]