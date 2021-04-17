from django.db import models

# Create your models here.

# TO DO
# remove blank = True & null = True 
class Event(models.Model):
    event_id = models.CharField(max_length = 100, blank = True)
    event_date = models.DateTimeField(null = True)
    page_title = models.CharField(max_length = 200, blank = True)
    page_description = models.CharField(max_length = 500, blank = True)
    page_tags = models.CharField(max_length = 100, blank = True)
    user_id = models.CharField(max_length = 100, blank = True)
    user_joined = models.DateTimeField(null = True)





