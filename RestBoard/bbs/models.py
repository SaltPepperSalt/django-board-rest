from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField('title', max_length=125, null=False)
    content = models.TextField('content', null=False)
    author = models.CharField('author', max_length=10, null=False)
    created_at = models.DateTimeField('created-date', auto_now_add=True)
    author.editable = False

    def __str__(self):
        return '[{}] {}'.format(self.id, self.title)
