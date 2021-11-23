from django.db import models

PROGRESS = (
  ('N', 'Not Started'),
  ('P', 'In Progress'),
  ('C', 'Completed')
)

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