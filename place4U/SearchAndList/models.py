from django.db import models
from django.utils import timezone
import datetime

class searchedTag(models.Model):
    searchedTag_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self) -> str:
        return str(self.searchedTag_text)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
# Create your models here.

class searchedList(models.Model):
    Tag = models.ForeignKey(searchedTag,on_delete=models.CASCADE)
    caption = models.CharField(max_length=3000)
    likes = models.IntegerField(default=0)
    place = models.CharField(max_length=200)
    def __str__(self) -> str:
        return str(self.Tag)