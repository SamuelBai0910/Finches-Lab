from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    s_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return f'{self.name} ({self.id})'
