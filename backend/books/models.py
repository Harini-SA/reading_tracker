from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    STATUS_CHOICES = [
        ('to_read', 'To Read'),
        ('reading', 'Reading'),
        ('finished', 'Finished'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    total_pages = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='to_read')
    cover_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ReadingLog(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='logs')
    date = models.DateField()
    pages_read = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.book.title} - {self.date}"

# Create your models here.
