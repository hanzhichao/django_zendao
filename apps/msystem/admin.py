from pprint import pprint

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User

admin.site.site_header = "禅道"
admin.site.site_title = "禅道"
admin.site.index_title = "禅道"


def get_app_list(self, request, app_label=None):
    app_dict = self._build_app_dict(request, app_label)

    if hasattr(settings, 'APP_LIST'):
        app_list_settings = getattr(settings, 'APP_LIST')
        pprint(app_list_settings)
        app_list = sorted(app_dict.values(),
                          key=lambda x: app_list_settings.get(x['app_label'])['order']
                          if x['app_label'] in app_list_settings else 100)

        for app in app_list:
            pprint(app['models'])
            model_settings = app_list_settings.get(app['app_label'], {}).get('models')
            if model_settings:
                app["models"].sort(
                    key=lambda x: model_settings.index(x["object_name"]) if x['object_name'] in model_settings else 100)
            else:
                app["models"].sort(key=lambda x: x["name"])

    else:
        app_list = sorted(app_dict.values(), key=lambda x: x["name"].lower())

        for app in app_list:
            app["models"].sort(key=lambda x: x["name"])

    return app_list


admin.AdminSite.get_app_list = get_app_list


@admin.register(admin.models.LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    """
    该类用于显示 admin 内置的 django_admin_log 表。
    其中，content_type 是指用户修改的 Model 名
    """
    list_display = ['action_time', 'user', 'content_type', '__str__']
    list_display_links = ['action_time']
    list_filter = ['action_time', 'content_type', 'user']
    list_per_page = 15
    readonly_fields = ['action_time', 'user', 'content_type',
                       'object_id', 'object_repr', 'action_flag', 'change_message']


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'last_name', 'first_name', 'is_active', 'last_login']
    list_display_links = ['username']

    filter_horizontal = ['groups', 'user_permissions']
    readonly_fields = ['date_joined', 'last_login']

    fields = ('username',
              'email',
              ('last_name', 'first_name'),
              ('is_active', 'is_staff', 'is_superuser'),
              'groups',
              'user_permissions',
              ('date_joined', 'last_login')
              )


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
