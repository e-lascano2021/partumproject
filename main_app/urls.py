from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('projects/', views.projects_index, name='projects_index'),
  path('projects/<int:project_id>/', views.projects_detail, name='projects_detail'),
  path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
  path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
  path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='projects_delete'),
  path('features/create/', views.FeatureCreate.as_view(), name='features_create'),
  path('features/', views.FeatureList.as_view(), name='features_index'),
  path('features/<int:pk>/update/', views.FeatureUpdate.as_view(), name='features_update'),
  path('features/<int:pk>/delete/', views.FeatureDelete.as_view(), name='features_delete'),
]