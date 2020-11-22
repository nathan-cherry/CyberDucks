from django.urls import path, re_path
from . import views

urlpatterns = [
    # Home Dashboard
    path('', views.home, name='home'),

    # Account Creation/ Login
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.signup, name='signup'),

    # Tasks
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create/', views.createTask, name='task_creation'),
    path('tasks/update/<str:task_id>', views.updateTask, name='update_task'),
    path('tasks/delete/<str:task_id>', views.deleteTask, name='delete_task'),
    path('tasks/<str:task_id>/', views.task, name='task_view'),

    # Notes
    path('notes/create/', views.createTask, name='note_creation'),
    path('notes/delete/<str:note_id>', views.deleteNote, name='delete_note'),

    # Projects
    path('projects/', views.home, name='projects'),
    path('projects/create/', views.home, name='projects_creation'),
    path('projects/update/<str:project_id>', views.home, name='projects_task'),
    path('projects/delete/<str:project_id>', views.home, name='projects_task'),
    path('projects/<str:project_id>/', views.home, name='projects_view'),
]
