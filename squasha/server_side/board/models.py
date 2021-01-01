from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Max
from django.utils import timezone



# Create your models here.

class Board(models.Model):
    #let's do the relational part after I've done the other fields
    title = models.CharField(max_length=255)
    Description = models.TextField(blank=True)
    #where I got the image https://mixkit.co/blog/trello-backgrounds-awesome-free-illustrations-for-trello-boards/
    ImageUrl = models.URLField(
    default="https://mixkit.imgix.net/art/preview/mixkit-starry-night-sky-over-hills-and-water-85-original-large.png?q=80&auto=format%2Ccompress&h=700&q=80&dpr=1",
    blank=True, null=False)
    CreatedAt = models.DateTimeField(default=timezone.now)
    #EndsAt = Board.return_date_time_in_one_year()

    def __str__(self):
        return self.title

    # Need to figure out how to write helper methods
    #@classmethod
    #def return_date_time_in_one_year():
    #    now = timezone.now()
    #    return now + timedelta(years=1)

class Column(models.Model):
    #add in relational fields

    Name = models.CharField(max_length=255)
    location = models.DecimalField(max_digits=1, decimal_places=0)

    def __str__(self):
        return self.Name

class Ticket(models.Model):
    # add in relational fields
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    TypeChoices = [('B','Bug'),('F','Feature'),('U','Urgent'),('S','Server Side'), ('C','Client Side')]
    Role = models.CharField(max_length=1, choices=TypeChoices)
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=True, null=True)
    # assigned_to = <-- also relational
    order = models.DecimalField(max_digits=3,decimal_places=0)

    def __str__(self):
        return self.title

# We're gonna need to put in a comment class
# And a notification class
