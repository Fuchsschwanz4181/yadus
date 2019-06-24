from django.db import models


class StoredUrls(models.Model):
    full_url = models.TextField()
    short_url = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.full_url
