from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Habitat(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('habitats_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    s_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    habitats = models.ManyToManyField(Habitat)
    
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    finch = models.ForeignKey(
        Finch, 
        on_delete=models.CASCADE
        )

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    # change the default sort
    class Meta:
        ordering = ['-date']