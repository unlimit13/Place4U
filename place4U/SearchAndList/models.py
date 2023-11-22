from django.db import models
from django.utils import timezone
import datetime

class searchedTag(models.Model):
    searchedTag_text = models.CharField(max_length=200)
    searchedLocation_text = models.CharField(max_length=100)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['searchedTag_text', 'searchedLocation_text'], name='unique_set'),
        ]
    pub_date = models.DateTimeField("date published")
    def __str__(self) -> str:
        return f"{self.searchedTag_text} - {self.searchedLocation_text}"
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
# Create your models here.

class searchedList(models.Model):
    tag_location = models.ForeignKey(searchedTag, on_delete=models.CASCADE, related_name='searched_lists')
    caption = models.CharField(max_length=3000)
    likes = models.IntegerField(default=0)
    place = models.CharField(max_length=200)
    def __str__(self) -> str:
        return str(self.tag_location)