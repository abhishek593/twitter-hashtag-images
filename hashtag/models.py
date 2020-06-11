from django.db import models
from django.utils import timezone
import json


class ScrapyItem(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    # img_url_list = models.TextField()
    data = models.TextField()  # One record contains 1 img url date and unique id which will be hashtag
    date = models.DateTimeField(default=timezone.now)

    @property
    def to_dict(self):
        data = {
            'data': json.loads(self.data),
            'date': self.date
        }
        return data

    def __str__(self):
        return self.unique_id

