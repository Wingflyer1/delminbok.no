from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_picture = models.TextField()
    story = models.TextField()
    readings = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    published = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    draft = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def book_summarys(self):
        story = self.story
        return story[:180]

    def story_to_lines(self):
        story = self.story
        lines_list = story.splitlines()
        return lines_list

    def printer(self):
        return "s"

    class Meta:
        ordering = ['-published']

        