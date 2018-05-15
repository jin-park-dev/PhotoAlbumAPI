from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    image = models.ImageField(upload_to='photo')

    viewed = models.IntegerField(default=0)
    liked = models.IntegerField(default=0)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    albums = models.ManyToManyField(Album)

    def __str__(self):
        try:
            return self.name
        except:
            return "unnamed"