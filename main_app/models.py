from django.db import models
from django.urls import reverse

PROGRESS = (
  ('N', 'Not Started'),
  ('P', 'In Progress'),
  ('C', 'Completed')
)

LEVELS = (
  ('E', 'Easy'),
  ('I', 'Intermediate'),
  ('D', 'Difficult'),
)

class Feature(models.Model):
  name = models.CharField(max_length = 50)
  difficulty = models.CharField(
    max_length = 1,
    choices = LEVELS,
    default = LEVELS[1][0]
  )

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("features_detail", kwargs={"pk": self.id})




class Project(models.Model):
  name = models.CharField(max_length=200)
  start_date = models.DateField('Start Date')
  end_date = models.DateField('End Date')
  description = models.TextField(max_length=350)
  progress = models.CharField(
  max_length=1,
  choices=PROGRESS,
  default=PROGRESS[0][0]
  )
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('projects_detail', kwargs={'project_id': self.id})
