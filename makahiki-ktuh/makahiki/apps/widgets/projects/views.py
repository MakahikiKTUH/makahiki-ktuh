"""Provides the view of the widget."""
import datetime
from apps.widgets.projects.models import Project, Goal, Comment
from apps.widgets.projects.forms import ProjectForm
from apps.widgets.projects import projects

def supply(request, page_name):
    """ supply view_object content, which is the projects for this game."""
    
    projects = list(Project.objects.filter(status="Approved"))
    goals = list(Goal.objects.all())
    comments = list(Comment.objects.all())
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            p = Project(title = form.cleaned_data['title'],
                        short_description = form.cleaned_data['short_description'],
                        long_description = form.cleaned_data['long_description'],
                        number_of_members = form.cleaned_data['number_of_members'],
            )
            p.deadline = datetime.datetime.today()
            p.save()
    else:
        form = ProjectForm()

    _ = request
    _ = page_name
    return {
        "projects": projects,    
        "goals": goals,
        "comments": comments,
        "form": form,
        }
