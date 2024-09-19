from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)  # Short text field for the post's title
    content = models.TextField()  # Large text field for the post's content
    author = models.CharField(max_length=50)  # Name of the post's author
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the post was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the post was last updated
    published = models.BooleanField(default=False)  # Boolean field indicating if the post is published
    views = models.IntegerField(default=0)  # Integer field for tracking the number of views
    category = models.CharField(max_length=50, null=True, blank=True)  # Optional category for the post

    def __str__(self):
        return self.title
