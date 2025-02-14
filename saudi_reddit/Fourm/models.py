# myredditapp/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from subreddit.models import Subreddit

class Post(models.Model):
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    isContentEdited = models.BooleanField(default=False)
    whenContentEdited = models.DateTimeField(default=None, blank=True, null=True)
    upvoters = models.ManyToManyField(User, related_name='upvoted_posts', blank=True)
    downvoters = models.ManyToManyField(User, related_name='downvoted_posts', blank=True)
    title = models.CharField(max_length=255,default='New Post')
    slug = models.SlugField(max_length=255,unique=True)
    views = models.IntegerField(default=0)
    content = models.TextField(default='New Post')
    image = models.ImageField(upload_to='images/posts/', blank=True)
    video = models.FileField(upload_to='videos/posts/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    votes = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug
            count = 1
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{count}"
                count += 1
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    isContentEdited = models.BooleanField(default=False)
    whenContentEdited = models.DateTimeField(default=None, blank=True, null=True)
    slug = models.SlugField(max_length=255,unique=True)
    image = models.ImageField(upload_to='images/comments/', blank=True)
    video = models.FileField(upload_to='videos/comments/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    upvoters = models.ManyToManyField(User, related_name='upvoted_comments', blank=True)
    downvoters = models.ManyToManyField(User, related_name='downvoted_comments', blank=True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.content)
            self.slug = base_slug
            count = 1
            while Comment.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{count}"
                count += 1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.content

