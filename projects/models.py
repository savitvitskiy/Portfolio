from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    repository = models.CharField(max_length=100, blank=True)
    image = models.FileField(upload_to="project_images/", blank=True)

    def __str__(self):
        return f"{self.title} {self.id}"
