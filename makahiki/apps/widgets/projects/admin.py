"""Energy goal widget administrator interface; shows the projects, actual vs. goal, last update."""

from django.contrib import admin
from apps.managers.challenge_mgr import challenge_mgr
from apps.widgets.projects.models import Comment, Goal, Project
from apps.admin.admin import challenge_designer_site, challenge_manager_site, developer_site

class ProjectAdmin(admin.ModelAdmin):
    """Project administrator interface definition."""
    list_display = ["title", "short_description", "long_description", "number_of_members",
                    "created", "deadline", "upvotes", "points", "status"]

admin.site.register(Project, ProjectAdmin)
challenge_designer_site.register(Project, ProjectAdmin)
challenge_manager_site.register(Project, ProjectAdmin)
developer_site.register(Project, ProjectAdmin)
challenge_mgr.register_designer_game_info_model("Projects", Project)
challenge_mgr.register_admin_game_info_model("Projects", Project)
challenge_mgr.register_admin_challenge_info_model("Projects", 1, Project, 1)
challenge_mgr.register_developer_challenge_info_model("Projects", 1, Project, 1)

class CommentAdmin(admin.ModelAdmin):
    """Comment administrator interface definition"""