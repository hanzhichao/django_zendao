from django.contrib import admin

from . import models

from utils.admin_utils import BaseAdmin, BaseTabularInline, BaseRecordAdmin, short_description


@admin.register(models.Project)
class ProjectAdmin(BaseAdmin):
    list_display = ('name', 'key', 'project_manager', 'end_date', 'status', 'work_days')
    fields = ('name', 'key', ('start_date', 'end_date', 'work_days'), 'team_name',
              ('type', 'status'),
              ('project_manager', 'product_manager'),
              ('test_manager', 'release_manager'),
              'description', 'view_control')

    class ProjectRelatedProductInline(BaseTabularInline):
        model = models.ProjectRelatedProduct

    class ProjectMemberInline(BaseTabularInline):
        model = models.ProjectMember

    inlines = [ProjectRelatedProductInline, ProjectMemberInline]


@admin.register(models.Task)
class TaskAdmin(BaseAdmin):
    class TaskAttachmentInline(BaseTabularInline):
        model = models.TaskAttachment

    inlines = [TaskAttachmentInline]

    list_display = ('level', 'name', 'status', 'end_date', 'assignee')
    fields = (
    ('project', 'product_module'), 'name', ('assignee', 'level'), ('type', 'status'), ('start_date', 'end_date'),
    'description', 'cc_to')
    filter_horizontal = ('cc_to',)
