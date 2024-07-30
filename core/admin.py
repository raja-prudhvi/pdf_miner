from django.contrib import admin
from .models import UploadedFile


@admin.register(UploadedFile)
class FileAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at",)
    readonly_fields = ("created_at", "text",)
