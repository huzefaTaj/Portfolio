from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to="media/images", default="")
    liveproject = models.URLField(max_length=500)
    code = models.URLField(max_length=500)

class Seo(models.Model):
    clicks=models.IntegerField(blank=True)