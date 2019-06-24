from django.contrib import admin
from .models import StoredUrls


class UrlsAdmin(admin.ModelAdmin):
    pass


admin.site.register(StoredUrls, UrlsAdmin)
