# Generated by Django 4.2.7 on 2023-12-13 10:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subreddit', '0003_alter_subreddit_author_alter_subreddit_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subreddit',
            name='subscribers',
            field=models.ManyToManyField(blank=True, default=None, related_name='subscribers', to=settings.AUTH_USER_MODEL),
        ),
    ]
