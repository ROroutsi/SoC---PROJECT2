# Generated by Django 3.0.4 on 2020-03-27 01:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-blogDate'], 'verbose_name': 'blog', 'verbose_name_plural': 'blogs'},
        ),
        migrations.AddField(
            model_name='blog',
            name='blogLikes',
            field=models.ManyToManyField(blank=True, related_name='blogLikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
