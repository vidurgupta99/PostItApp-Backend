from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('postits/', views.getPostIts, name="postits"),
    path('postits/<str:pk>/', views.getPostIt, name="postit"),