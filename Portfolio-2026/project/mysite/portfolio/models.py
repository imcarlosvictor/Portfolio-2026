from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True)
    title = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='static/media/images/', blank=True)
    description = models.TextField(max_length=400, db_index=True)
    # tech_stack = ArrayField(models.CharField(max_length=20, blank=True), default=list)
    github_url = models.CharField(max_length=300, null=True, default='', blank=True)
    live_url = models.CharField(max_length=300, null=True, default='', blank=True)

    class Meta:
        ordering = (('id'),)
        index_together = (('id'), ('slug'),)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('', args=[self.id, self.slug])