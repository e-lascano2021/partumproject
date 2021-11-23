from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from .models import Project, Feature, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'partum-project'


def about(request):
  return render(request, 'about.html')

@login_required
def projects_index(request):
  projects = Project.objects.filter(user=request.user)
  return render(request, 'projects/index.html', { "projects" : projects })

@login_required
def projects_detail (request, project_id):
  project = Project.objects.get(id=project_id)
  features_project_doesnt_have = Feature.objects.exclude(id__in = project.features.all().values_list('id'))
  return render(request, 'projects/detail.html', {
    'project': project,
    'features': features_project_doesnt_have})

@login_required
def assoc_feature(request, project_id, feature_id):
  Project.objects.get(id=project_id).features.add(feature_id)
  return redirect('projects_detail', project_id=project_id)

@login_required
def unassoc_feature(request, project_id, feature_id):
  Project.objects.get(id=project_id).features.remove(feature_id)
  return redirect('projects_detail', project_id=project_id)

@login_required
def add_photo(request, project_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, project_id=project_id)
      project_photo = Photo.objects.filter(project_id=project_id)
      if project_photo.first():
        project_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('projects_detail', project_id=project_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)




class Home(LoginView):
  template_name = 'home.html'

class ProjectCreate(LoginRequiredMixin, CreateView):
  model = Project
  fields = ['name', 'progress', 'start_date', 'end_date', 'description']
  success_url = '/projects/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class ProjectUpdate(LoginRequiredMixin, UpdateView):
  model = Project
  fields = '__all__'

class ProjectDelete(LoginRequiredMixin, DeleteView):
  model = Project
  success_url = '/projects/'

class FeatureCreate(LoginRequiredMixin, CreateView):
  model =  Feature
  fields = '__all__'

class FeatureList(LoginRequiredMixin, ListView):
  model = Feature

class FeatureUpdate(LoginRequiredMixin, UpdateView):
  model = Feature
  fields = '__all__'

class FeatureDelete(LoginRequiredMixin, DeleteView):
  model = Feature
  success_url = '/features/'