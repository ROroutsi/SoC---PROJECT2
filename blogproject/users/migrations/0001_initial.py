# Generated by Django 3.0.4 on 2020-03-23 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('commentAuthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentAuthor', to=settings.AUTH_USER_MODEL)),
                ('commentBlog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentBlog', to='blogs.blog')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]