from django.db import models
from django.contrib.auth.models import User
from stories.models import Book

class Comment(models.Model):
    # comment = models.CharField(max_length = 148, blank=True)
    dice = models.IntegerField(default=0, verbose_name='Terningkast')
    book = models.ForeignKey(Book, verbose_name='Bok')
    comment_writer = models.ForeignKey(User, verbose_name='Kommentar fra')
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.book.title

    def __unicode__(self):
        return self.book.title

    class Meta:
        ordering = ['-created']
