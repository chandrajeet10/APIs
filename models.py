from django.db import models

class ToDo(models.Model):
    Title = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    Date = models.DateField(blank=False)


    def __str__(self):
        return self.Title  

