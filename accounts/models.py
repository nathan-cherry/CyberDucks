import uuid

from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    # id = models.AutoField(primary_key=True)
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=256, null=True)
    description = models.TextField(null=True, blank=True)
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('OPN', 'Open'),
        ('COM', 'Completed'),
        ('SUS', 'Suspended'),
    ]
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=0,
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    client_name = models.CharField(max_length=256, null=True, blank=True)
    client_email = models.EmailField(max_length=256, null=True, blank=True)
    repo = models.URLField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=256, null=True)
    description = models.TextField(null=True, blank=True)
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('OPN', 'Open'),
        ('COM', 'Completed'),
        ('SUS', 'Suspended'),
    ]
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=0,
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    PRIORITY_CHOICES = [
        ('LW', 'Low'),
        ('MD', 'Medium'),
        ('HI', 'High'),
        ('CR', 'Critical'),
    ]
    priority = models.CharField(
        max_length=2,
        choices=PRIORITY_CHOICES,
        default=0,
    )
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Note(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=256, null=True)
    note = models.TextField(null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
