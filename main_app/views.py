from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Project, Feature


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def projects_index(request):
  projects = Project.objects.all()
  return render(request, 'projects/index.html', { "projects" : projects })

def projects_detail (request, project_id):
  project = Project.objects.get(id=project_id)
  features_project_doesnt_have = Feature.objects.exclude(id__in = project.features.all().values_list('id'))
  return render(request, 'projects/detail.html', {
    'project': project,
    'features': features_project_doesnt_have})

def assoc_feature(request, project_id, feature_id):
  Project.objects.get(id=project_id).features.add(feature_id)
  return redirect('projects_detail', project_id=project_id)

def unassoc_feature(request, project_id, feature_id):
  Project.objects.get(id=project_id).features.remove(feature_id)
  return redirect('projects_detail', project_id=project_id)

class ProjectCreate(CreateView):
  model = Project
  fields = ['name', 'progress', 'start_date', 'end_date', 'description']
  success_url = '/projects/'

class ProjectUpdate(UpdateView):
  model = Project
  fields = '__all__'

class ProjectDelete(DeleteView):
  model = Project
  success_url = '/projects/'

class FeatureCreate(CreateView):
  model =  Feature
  fields = '__all__'

class FeatureList(ListView):
  model = Feature

class FeatureUpdate(UpdateView):
  model = Feature
  fields = '__all__'

class FeatureDelete(DeleteView):
  model = Feature
  success_url = '/features/'