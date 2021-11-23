from django.shortcuts import render



class Project:
  def __init__ (self, name, start_date, end_date, description, progress):
    self.name = name
    self.start_date = start_date
    self.end_date = end_date
    self.description = description
    self.progress = progress
    

projects = [
  Project("Stack 4", "Sept", "Late Sept", "basically a connect 4 game", "Completed"),
  Project("Music Mania", "Oct", "Nov", "a playlist website", "Not Started"),
  Project("Partum Projects", "Early Nov", "Late Nov", "A project Organizer", "In Progress"),
]






def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def projects_index(request):
  return render(request, 'projects/index.html', { "projects" : projects })