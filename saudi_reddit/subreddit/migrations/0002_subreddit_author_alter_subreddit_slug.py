# Generated by Django 4.2.7 on 2023-12-06 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subreddit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subreddit',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subreddit',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
