from django.db import models

# Create your models here.
class ProjectInfo(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    link = models.URLField(blank=True)
    github = models.URLField(blank=True)
    demo = models.CharField(max_length=30, blank=True)
    image = models.FileField(upload_to="photos/projects", blank=True)
    show = models.BooleanField(default=False)
    priority = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class Experience(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    link = models.URLField(blank=True)
    image = models.FileField(upload_to="photos/experiences", blank=True)
    show = models.BooleanField(default=False)
    priority = models.IntegerField(default=10)

    def __str__(self):
        return self.name
