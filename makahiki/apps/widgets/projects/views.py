"""Provides the view of the widget."""
import datetime
from apps.widgets.projects.models import Project, Goal, Comment
from apps.widgets.projects.forms import ProjectForm, GoalForm
from apps.widgets.projects import projects

def supply(request, page_name):
    """ supply view_object content, which is the projects for this game."""
    
    today = datetime.date.today()
    projects = Project.objects.filter(status="Approved").filter(deadline__lte=today)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        gforms = [GoalForm(request.POST, prefix=str(x), instance=Goal()) for x in range(0,5)]
        if form.is_valid():
            p = Project(title = form.cleaned_data['title'],
                        short_description = form.cleaned_data['short_description'],
                        long_description = form.cleaned_data['long_description'],
                        number_of_members = form.cleaned_data['number_of_members'],
                        deadline = form.cleaned_data['deadline'],
            )
            p.save()
            for gf in gforms:
                if gf.is_valid() and not gf.has_no_text_or_deadline:
                    new_goal = gf.save(commit=False)
                    new_goal.project = p
                    new_goal.save()
    else:
        form = ProjectForm()
        gforms = [GoalForm(prefix=str(x), instance=Goal()) for x in range(0,5)]
    _ = page_name
    return {
        "projects": projects,    
        "form": form,
        "gforms": gforms,
        }
