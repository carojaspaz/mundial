"""
URL configuration for mundial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from album import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('selection/', views.SelectionListView.as_view(), name='selection-list'),
    path('selection/create/', views.SelectionCreate.as_view(),
         name='selection-create'),
    path('selection/<int:pk>/detail/',
         views.SelectionDetailView.as_view(), name='selection-detail'),
    path('player/', views.PlayerListView.as_view(), name='player-list'),
    path('player/<int:pk>/detail/',
         views.PlayerDetailView.as_view(), name='player-detail'),
    # Update
    path('player/<int:pk>/update/',
         views.PlayerUpdate.as_view(), name='player-update'),
    # Create
    path('player/<int:pk>/create/',
         views.PlayerCreate.as_view(), name='player-create'),
    # Delete
    path('player/<int:pk>/delete/',
         views.PlayerDelete.as_view(), name='player-delete'),
]
