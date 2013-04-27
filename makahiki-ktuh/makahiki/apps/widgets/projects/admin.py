"""Energy goal widget administrator interface; shows the projects, actual vs. goal, last update."""

from django.contrib import admin


class ProjectAdmin(admin.ModelAdmin):
    """Project administrator interface definition."""
    list_display = ["title", "short_description", "long_description", "number_of_members",
                    "created", "deadline", "upvotes", "points", "status"]


"""
admin.site.register(Project, ProjectAdmin)
challenge_designer_site.register(Project, ProjectAdmin)
challenge_manager_site.register(Project, ProjectAdmin)
developer_site.register(Project, ProjectAdmin)

challenge_mgr.register_designer_game_info_model("Projects", Project)
challenge_mgr.register_admin_game_info_model("Projects", Project)
"""