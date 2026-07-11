from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    summary = models.TextField()
    content = models.TextField()

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    published_at = models.DateTimeField(default=timezone.now)

    tags = models.ManyToManyField(
        Tag,
        related_name="posts",
        blank=True,
    )

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title