from rest_framework import serializers
from .models import Book, ReadingLog

class ReadingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingLog
        fields = ['id','book','date','pages_read','notes']

class BookSerializer(serializers.ModelSerializer):
    logs = ReadingLogSerializer(many = True, read_only=True)
    class Meta:
        model = Book
        fields = ['id','title','author','total_pages','status','cover_url','created_at','logs']
        read_only_fields = ['user']
