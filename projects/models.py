from django.db import models
from django.template.defaultfilters import slugify

class ProjectManager(models.Manager):
    def create_project(self, name, slug, description):
        if len(slug) == 0:
            slug = slugify(name)

        return self.create(name=name, slug=slug, description=description)

class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()

    objects = ProjectManager()