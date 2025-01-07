from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

# Create your models here.

class Video(models.Model):
    #all video fields
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    video_file = models.FileField(upload_to='uploads/video_files', validators = [FileExtensionValidator(allowed_extensions=['mp4'])])
    thumbnail = models.FileField(upload_to='uploads/thumbnail', validators = [FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    date_posted = models.DateTimeField(default=timezone.now)

class Collection(models.Model):
    title = models.CharField(max_length=100, default='New Collection')
    video_count = models.IntegerField()
    videos = models.ManyToManyField(Video, related_name='collections')