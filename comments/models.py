from django.db import models
from django.contrib.auth.models import User
from stories.models import Book

class Comment(models.Model):
    comment = models.CharField(max_length = 148)
    book = models.ForeignKey(Book)
    comment_writer = models.ForeignKey(User)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.comment

    def __unicode__(self):
        return self.comment
