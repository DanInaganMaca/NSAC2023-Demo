from django.utils import timezone
from django.db import models

# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=50, null=False)
    name_tab = models.CharField(max_length=50, null=False)
    create_at = models.DateField(null=False, default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.create_at:
            self.create_at = timezone.now()
        super().save(*args, **kwargs)


class ContentType(models.Model):
    name = models.CharField(max_length=50, null=False)
    create_at = models.DateField(null=False, default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.create_at:
            self.create_at = timezone.now()
        super().save(*args, **kwargs)


class Content(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    image_url = models.TextField(null=True)
    video_url = models.TextField(null=True)
    theme = models.IntegerField(null=False)
    create_at = models.DateField(null=False, default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.create_at:
            self.create_at = timezone.now()
        super().save(*args, **kwargs)
