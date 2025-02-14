# Generated by Django 4.2.7 on 2023-12-06 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subreddit', '0002_subreddit_author_alter_subreddit_slug'),
        ('Fourm', '0002_alter_post_subreddit_delete_subreddit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Subreddit',
        ),
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='subreddit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subreddit.subreddit'),
        ),
    ]
