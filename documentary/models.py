from django.db import models

# Create your models here.
class Title(models.Model):
    """docstring for title"""
    title_name = models.CharField(max_length=512)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title_name

class Author(models.Model):
    """docstring for Author"""
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Site(models.Model):
    """docstring for site"""
    title = models.ForeignKey(Title)
    author = models.ForeignKey(Author)
    seed = models.CharField(max_length=1024)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.seed)
