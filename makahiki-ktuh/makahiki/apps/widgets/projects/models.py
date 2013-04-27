'''
Created on Apr 16, 2013

@author: davey
'''

"""Implements the model for project management."""
from django.db import models
from apps.managers.player_mgr import player_mgr
from apps.managers.resource_mgr import resource_mgr

from apps.managers.team_mgr import team_mgr
from apps.managers.team_mgr.models import Group, Team
from apps.utils.utils import media_file_path


_MEDIA_LOCATION = "projects"
"""location for uploaded files."""


class Project(models.Model):
    """Represents a project in the system."""
    STATUS_CHOICES = (("Suggested", "Suggested"),
                    ("Approved", "Approved"),
                    ("Finished", "Finished"),)

    created = models.DateField(auto_now_add=True) 

    title = models.CharField(
        max_length=75, 
        help_text="The title of the project.")
    
    short_description = models.TextField(
        max_length="300",
        help_text="Short description of the project. This should include information about its "
                  "goal. It is usually displayed in the project list page.")
    long_description = models.TextField(
        max_length="5000",
        help_text="Detailed information about the project. It is usually displayed in the details "
                  "view of the project.")
    
    number_of_members = models.IntegerField(
        default=1,
        help_text="Minimum is 1 member, maximum is 100.")
    
    status = models.CharField(
        default="Suggested",
        choices=STATUS_CHOICES,
        max_length=20,
        help_text="The status of the project.")
    
    deadline = models.DateField(
        auto_now_add=True, 
        help_text="The last day on which the project "
                  "can be completed to count for points.")

    upvotes = models.IntegerField(default=0)
    points = models.IntegerField(
        default=0, 
        help_text="The value of the project.")

    
class Goal(models.Model):
    project = models.ForeignKey(Project)
    text = models.CharField(max_length=100, help_text="The goal or step for the project's progress.")
    deadline = models.DateTimeField()
    finished = models.BooleanField(default=False)
        
    
class Comment(models.Model):
    project = models.ForeignKey(Project)
    created = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=3000)
    player = models.CharField(max_length=100)
    

#this possibly has to go (to be replaced by a user_mgr function?)
class Player(models.Model):
    project = models.ForeignKey(Project)
    name =  models.CharField(max_length=100)
    