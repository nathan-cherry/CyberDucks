from .forms import *
from datetime import datetime


def getTasksToday(request):
    task_list = Task.objects.filter(assigned_to__exact=request.user, end_date__contains=datetime.now().date()).exclude(
        status__exact='COM')
    return task_list


def projectCompletion(request):
    project_percentage = []
    project_list = Project.objects.filter(assigned_to__exact=request.user)
    for project in project_list:
        task_list = Task.objects.filter(project__id__exact=project.id)
        completed = task_list.filter(status__exact='COM').count()
        suspended = task_list.filter(status__exact='SUS').count()
        print("Total: " + str(task_list.count()))
        print("Suspended: " + str(suspended))
        print("Complete: " + str(completed))
        total_tasks = task_list.count() - suspended
        if total_tasks != 0:
            percentage = round((completed / total_tasks) * 100)
        else:
            percentage = 0
        if percentage != 100:
            project_percentage.append({
                'project': project,
                'total': total_tasks,
                'completed': completed,
                'percentage': percentage
            })

    return project_percentage
