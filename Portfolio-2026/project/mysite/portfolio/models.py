from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
# from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True)
    title = models.CharField(max_length=200, db_index=True)
    # image = models.ImageField(upload_to='static/media/images/', blank=True)
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
    
class ProjectMedia(models.Model):
    IMAGE = 'image'
    VIDEO = 'video'
    MEDIA_TYPES = [
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='media_list')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='static/media/images/')
    order = models.PositiveIntegerField(default=0)

    def clean(self):
        super().clean()
        media = self.project.media_list.all()

        image_count = media.filter(media_type='image').count()
        video_count = media.filter(media_type='video').count()

        if self.media_type == 'image' and image_count >= 4:
            raise ValidationError('A project must have 4 images.')
        if self.media_type == 'video' and image_count >= 1:
            raise ValidationError('This project has a video demo.')