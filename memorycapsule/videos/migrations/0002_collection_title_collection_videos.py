# Generated by Django 5.1.4 on 2025-01-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='title',
            field=models.CharField(default='New Collection', max_length=100),
        ),
        migrations.AddField(
            model_name='collection',
            name='videos',
            field=models.ManyToManyField(related_name='collections', to='videos.video'),
        ),
    ]
