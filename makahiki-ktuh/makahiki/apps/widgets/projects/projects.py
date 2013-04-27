'''
Created on Apr 17, 2013

@author: shindig
'''
from apps.widgets.projects.models import Project, Goal, Comment


def get_current_projects():
    projects = list(Project.objects.filter(status="Approved"))
    goals = list(Goal.objects.all())
    comments = list(Comment.objects.all())
    
