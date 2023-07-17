from django.db import models
from django.urls import reverse

class UploadedFile(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.file.name

    def get_absolute_url(self):
        return reverse('pdf_miner:uploaded_file_detail', kwargs={'pk': self.pk})
